import socket
import tqdm

host = '192.168.43.33'
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

client, addr = server.accept()

gen_message = client.recv(1024).decode()
gen_message = gen_message.split('\n')
conn_messsage = gen_message[0]
file_name = gen_message[1]
file_name = f'Received_{file_name}'
file_size = gen_message[2]
end_message = gen_message[3]

print(conn_messsage)
print(file_name)
print(file_size)

done = False

progress = tqdm.tqdm(unit="MB", unit_scale = True, unit_divisor = 1024, 
                     total = int(file_size))

with open(file_name, 'wb') as file:
    while not done:
        data = client.recv(1024)
        if data:
            file.write(data)
            progress.update(len(data))
        else:
            done = True 

client.close()
server.close()

