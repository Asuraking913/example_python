import socket
import sys

host = socket.gethostbyname(socket.gethostname())
port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((host, port))
except Exception as e:
    print(f'Error: {e}')

server.listen()

client, addr = server.accept()

handshake = client.recv(1024).decode()
print(handshake)

client.send("Received Handshake!!".encode())

    
