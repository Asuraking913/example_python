import socket
import tqdm
import os

host = socket.gethostbyname(socket.gethostname())
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((host, port))
except Exception as e:
    pass
server.listen()

client, addr = server.accept()
#split gen message
gen_message = client.recv(1024).decode()
gen_message = gen_message.split('\n')
conn_message = gen_message[0]
file_path = gen_message[1]
file_name = file_path.split('/')[-1]
file_name = f'Received_{file_name}'
file_size = gen_message[2]
end_message = gen_message[3]
len_files = gen_message[4]


print(conn_message)
# print(file_name)
print(file_size)



progress = tqdm.tqdm(unit = "MB", unit_scale = True, unit_divisor = 1024, 
                total = int(file_size))

done = False
# with open(file_name, 'wb') as file:
#     while not done:
#         data = client.recv(buffer)
#         if data:
#             file.write(data)
#         else:
#             done = True
#         progress.update(len(data))
file = open(file_name, 'wb')
for i in range(len(len_files)):
    while not done:
        data = client.recv(1024)
        if b'end' not in data:
            file.write(data)
            progress.update(len(data))
        else:
            done = True
    print(file_name)

print(end_message)