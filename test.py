import os
import client

content = os.walk("/home/asura/Desktop/codeverse/python/example_python/new2")
list_tree = list(content)
# print(list_tree)

# for n in range(len(list_tree)):
#     print(list_tree[n])

for dir, folder_list, files_list in list_tree:
    for files in files_list:
        client.send_file(f'{dir}/{files}', len(list_tree))

# print(list_tree)
# client.send_file("/home/asura/Desktop/codeverse/python/example_python/new2/distsdf/sdf/sa.txt")

# for dir, folder, files in list_tree:
#     print(dir)
#     print(folder)
#     print(files)