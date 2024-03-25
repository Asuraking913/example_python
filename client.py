import socket
import os
import tqdm

def send_file(file_path, len_files):
    host = socket.gethostbyname(socket.gethostname())
    port = 9999

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except ConnectionRefusedError:
        pass

    file_name = file_path.split("/")[-1]
    file_size = os.path.getsize(file_path)
    conn_message = "Connection Initated"
    end_message = "Connection Ended"
    try:
        client.send((conn_message + '\n' + file_name + '\n' + str(file_size) + '\n' + end_message + '\n' + len_files).encode())
    except BrokenPipeError:
        pass

    progress = tqdm.tqdm(unit="MB", unit_scale=True, unit_divisor=1024, 
                        total=int(file_size))

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if data:
                try:
                    client.sendall(data)
                    progress.update(len(data))
                except Exception as e:
                    print(f"Error: {e}")
                    pass
            else:
                client.send('end'.encode())
                break
    client.close()

