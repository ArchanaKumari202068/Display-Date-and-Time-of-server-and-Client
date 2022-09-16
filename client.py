# client.py
import socket
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)
print(f"Received {data!r}")












"""

from http import client
from socket import *
import time
import datetime
import sys
servername = "127.0.0.1" # IP address
serverport =1000
clientsocket = socket(AF_INET,SOCK_STREAM)

ping = "ping"
print("date of sending request by client is " + str(datetime.datetime.now()))
start_time = time.time()


# clientsocket.send(ping.encode())
# date= clientsocket.recv(2048).decode()
# recv_time = time.time()
# time_taken=recv_time-start_time

# print("time taken is : " + str(time_taken)+"s")
# print("date recieved is " + str(date))
# clientsocket.close()


"""