from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_socketio import SocketIO, emit

# Le mot de passe est : pass

class Color:
    GREEN = "\033[1;92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RED = "\033[1;91m"


print(Color.BLUE + """
                                CREATED BY VOUTOUZ AND B4ptisteC    
""")


onlineMember = 0
app = Flask(__name__)
app.config["SECRET_KEY"] = "chatEnLigne!"
socketio = SocketIO(app)



### @app.route


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
    
        if password == 'pass':
            session['logged_in'] = True 
            return redirect(url_for('main'))
        else:
            flash('Mot de passe incorrect')
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
    return render_template("general.html")

@app.route("/lycee.html")
def lycee():
    if not session.get('logged_in'):
        flash('Vous devez vous connecter pour accéder à cette page')
        return redirect(url_for('login'))
    return render_template("lycee.html")

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@socketio.on("connect")
def newConnection():
    global onlineMember
    onlineMember += 1
    emit("server response", f"=> Quelqu’un a rejoint le chat  - {onlineMember} membre connecté(s)", broadcast=True)

@socketio.on("disconnect")
def disconnection():
    global onlineMember
    onlineMember -= 1
    emit("server response", f"<= Quelqu’un a quitter le chat - {onlineMember} membre connecté(s)", broadcast=True)

@socketio.on("message")
def handle_message(data):
    emit("server response", data, broadcast=True)

###

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5001, ssl_context=("cert.pem", "key.pem"))
