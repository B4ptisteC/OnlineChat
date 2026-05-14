from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_socketio import SocketIO, emit
import json
import os

class Color:
    GREEN = "\033[1;92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RED = "\033[1;91m"

print(Color.BLUE + """
                                CREATED BY VOUTOUZ AND B4ptisteC    
""")

def load_users():
    """Charge les utilisateurs depuis le fichier users.json"""
    users_file = os.path.join(os.path.dirname(__file__), "users.json")
    with open(users_file, "r", encoding="utf-8") as f:
        return json.load(f)

onlineMember = 0
app = Flask(__name__)
app.config["SECRET_KEY"] = "chatEnLigne!"
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        users = load_users()

        if username in users and users[username] == password:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('main'))
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route("/main")
def main():
    if not session.get('logged_in'):
        flash('Vous devez vous connecter pour accéder à cette page')
        return redirect(url_for('login'))
    return render_template("main.html")

@app.route("/general.html")
def server():
    if not session.get('logged_in'):
        flash('Vous devez vous connecter pour accéder à cette page')
        return redirect(url_for('login'))
    return render_template("general.html", username=session.get('username'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@socketio.on("connect")
def newConnection():
    global onlineMember
    onlineMember += 1
    username = session.get('username', 'Anonyme')
    emit("server response", {
        "type": "system",
        "content": f"=> {username} a rejoint le chat  - {onlineMember} membre(s) connecté(s)"
    }, broadcast=True)

@socketio.on("disconnect")
def disconnection():
    global onlineMember
    onlineMember -= 1
    username = session.get('username', 'Anonyme')
    emit("server response", {
        "type": "system",
        "content": f"<= {username} a quitté le chat - {onlineMember} membre(s) connecté(s)"
    }, broadcast=True)

@socketio.on("message")
def handle_message(data):
    username = session.get('username', 'Anonyme')
    emit("server response", {
        "type": "message",
        "username": username,
        "content": data
    }, broadcast=True)

###

if __name__ == "__main__":
    import ssl
    import eventlet
    import eventlet.wsgi

    ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_ctx.load_cert_chain("cert.pem", "key.pem")

    sock = eventlet.listen(("0.0.0.0", 5001))
    sock = eventlet.wrap_ssl(sock,
                             certfile="cert.pem",
                             keyfile="key.pem",
                             server_side=True)

    print(Color.GREEN + " * Running on https://127.0.0.1:5001")
    eventlet.wsgi.server(sock, app)
