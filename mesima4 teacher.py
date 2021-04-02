import random
import os
from colorama import init
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

def printInColor(sentence, number):
    #1
    # if number == 1:
    #     print(f"{Fore.RED}", end="")
    # if number == 2:
    #     print(f"{Fore.YELLOW}", end="")
    # if number == 3:
    #     print(f"{Fore.BLUE}", end="")
    # if number == 4:
    #     print(f"{Fore.GREEN}", end="")
               
    # print(f"{sentence}{Style.RESET_ALL}")   
    #2
    colors = [Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.GREEN]
    print(f"{colors[number-1]}{sentence}{Style.RESET_ALL}")


name = input("type your name: ")
number=int(input("choose a color (1-red, 2-yellow, 3-blue, 4-green): "))
print("your name is: ", end="")

printInColor(name, number)