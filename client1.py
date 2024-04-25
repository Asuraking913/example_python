import socket
import sys

host = socket.gethostbyname(socket.gethostname())
port = 9999
payload = 'Hey there, i am connected'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        client.connect((host, port))
        client.send(payload.encode())
        break
    except Exception as e:
        print(f'Error: {e}')
exchange = client.recv(1024).decode()
print(exchange)


    # payload = 'Hey there!!'.encode()
    # client.send(payload)
    # gen_message = client.recv(1024).decode()
    # print(gen_message)