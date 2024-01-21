from os import system
from os import getcwd
from os import listdir

def run_commit1():
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
    
    def run_commit2(message):
        return system(f"{message}")
    
    def run_url(url):
        return system(f"{url}")

    if ".git" in file_list:
        run_add()
        run_commit1()
        run_push()
    else:
        run_init()
        run_add()
        message = input("Enter your git message")
        run_commit2()
        url = input("Enter your remote url: ")
        run_url(url)

        run_push()


run_cmd()
