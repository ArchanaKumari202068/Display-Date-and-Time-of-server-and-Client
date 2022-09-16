# server.py
import socket
from datetime import datetime
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket succesfully created")
    s.bind((HOST, PORT))
    print(f"Socket succesfully binded to {PORT}")
    s.listen()
    print("socket is listening")
    connection, addr = s.accept()
    with connection:
        print(f"Connected by {addr}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            data = str(datetime.now()).encode()
            connection.sendall(data)