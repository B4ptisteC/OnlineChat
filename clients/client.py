import socketio

print("""
                                CREATED BY VOUTOUZ AND B4ptisteC    
""")

sio = socketio.Client()

@sio.event
def connect():
    print("Connected!")
    while True:
        message = input("Enter your message: ")
        sio.emit("message", message)

@sio.on("server response")
def response(data):
    print("\nReceived response:", data)
    print("Enter your message: ")

server_ip = input("Enter the IP address: ")
sio.connect("https://" + server_ip + ":5000")
sio.wait()
