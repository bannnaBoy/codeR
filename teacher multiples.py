import os
import random
import time
import colorama
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

import random
import os

from colorama import init
from colorama import Fore, Back, Style, init

init()


def cls(): return os.system('cls')


cls()

def compute(a, b):
    if a%b==0:
        print(f"{a} is multiple of {b}: {a}/{b}={int(a/b)}")
    else:
        print(f"{a} is not multiple of {b}")
        multiples=" "
        for x in range(2,a): #a=12   2 3 4 5 6 7 8 9 10 11 
            if a%x==0:
                multiples = multiples+str(x)+"("+str(x)+"x"+str(int(a/x))+")   "
        if multiples=="":
            print(f"{a} is a prime number")
        else:
            print(f"but {a} is multiple of {multiples}")



a = int(input("first number: "))
b = int(input("second number: "))
compute(a, b)