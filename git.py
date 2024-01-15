from os import system
from os import listdir
import os

def run_git():
    files = os.listdir("/home/asuraking/Desktop/codeverse/PYTHON/Prog-example")
    if ".git" in files:
        return system("git add .")
        return system("git commit -m 'new changes'")
    else:
        return system("git init")
        return system("git add .")
        return system("git commit -m 'new changes'")

run_git()