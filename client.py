import socket

host = socket.gethostbyname(socket.gethostname())
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((host, port))
except ConnectionRefusedError:
    pass

client.send()
