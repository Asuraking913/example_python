from os import system
from os import listdir
import os

def run_add():
    return system("git add .")

def run_commit():
    return system("git commit -m 'new changes'")

def run_init():
        return system("git init")


def run_git():
    files = os.listdir("/home/asuraking/Desktop/codeverse/PYTHON/Prog-example")
    if ".git" in files:
        run_add()
        run_commit()
    else:
        run_add()
        run_commit()

run_git()