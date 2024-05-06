# import os

# def get_folder_size(folder_path):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(folder_path):
#         for filename in filenames:
#             file_path = os.path.join(dirpath, filename)
#             total_size += os.path.getsize(file_path)
#     return total_size

# folder_path = '/home/asura/Desktop/codeverse/python/Transfer_app/GTA San Andreas'
# folder_size_bytes = get_folder_size(folder_path)

# # Convert bytes to MB or GB for readability
# folder_size_mb = folder_size_bytes / (1024 * 1024)
# folder_size_gb = folder_size_bytes / (1024 * 1024 * 1024)

# print(f"Total size of folder '{folder_path}':")
# print(f"{folder_size_bytes} bytes")
# print(f"{folder_size_mb:.2f} MB")
# print(f"{folder_size_gb:.2f} GB")


from tqdm import tqdm
import time


import time
from tqdm import tqdm

import time
from tqdm import tqdm

def my_function():
    a = 0
    for _ in tqdm(range(100000), desc="Processing", unit="iteration"):
        a += 1
        # Simulate some computation
        time.sleep(0.00001)

my_function()


