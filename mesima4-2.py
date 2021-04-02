import os
import random
import time
import colorama
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

def compute(a,b):
    if a%b==0:
        print(f"{a} is a multiple of {b}: {a}/{b}={a/b}")
    else:
        print(f"{a} is not a multiple of {b}")    