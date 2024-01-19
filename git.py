from os import system
from os import getcwd
from os import listdir

def run_commit():
    return system("git commit -m 'new changes'")

def run_push():
    return system("git push origin master")

def run_add ():
    return system("git add .")

def run_init():
    return system("git init")

def run_cmd():
    file_path = getcwd()
    file_list = listdir(file_path)
    
    if ".git" in file_list:
        run_add()
        run_commit()
        run_push()
    else:
        run_init()
        run_add()
        run_commit()
        run_push()


run_cmd()
