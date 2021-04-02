import os
import random
import time
import colorama
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

sentence = str(input("Type sentence: "))
color = str(input("Type a color: "))

def printRed(s):
    print(f"{Fore.RED}{s}{Style.RESET_ALL}")
def printYellow(s):
    print(f"{Fore.YELLOW}{s}{Style.RESET_ALL}")
def printBlue(s):
    print(f"{Fore.BLUE}{s}{Style.RESET_ALL}")        
def printGreen(s):
    print(f"{Fore.GREEN}{s}{Style.RESET_ALL}")    

if color == "red":
    print("Your sentence is: ", end="")
    printRed(sentence)
if color == "yellow":
    print("Your sentence is: ", end="")
    printYellow(sentence)
if color == "blue":
    print("Your sentence is: ", end="")
    printBlue(sentence)
if color == "green":
    print("Your sentence is: ", end="")
    printGreen(sentence)            