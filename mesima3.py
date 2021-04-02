import os
import random
import colorama
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

name = input("Type your name here: ")
print(f"You have {len(name)} letters in your name ")
print("The letters of your name are:")

for x in range(len(name)):
    if x % 2 == 0:
        print(f"{Fore.RED} {name[x]}", end="")
    else:
        print(f"{Fore.GREEN} {name[x]}", end="")