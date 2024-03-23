import os

content = os.walk("/home/asura/Desktop/codeverse/python/Transfer_app/version2/GTA San Andreas")
list_tree = list(content)
# print(list_tree)

# for n in range(len(list_tree)):
#     print(list_tree[n])

# print(list_tree[0])
# print(list_tree[1])
# print(list_tree[2])

for dir, folder, files in list_tree:
    print(dir)
    print(folder)
    print(files)