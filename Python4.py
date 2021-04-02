import os
import random
import time
import colorama
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

def Red(s):
    print(f"{Fore.RED}{s}{Style.RESET_ALL}")

def printYellow(s):
    print(f"{Fore.YELLOW}{s}{Style.RESET_ALL}", end=" ")   

def inputBlue(s):
    return f"{s}{Fore.BLUE}"

# a = input(inputBlue("TEST: "))
# printRed("Test")
# printYellow("Test")  
print()
word =["banana","elephant","hotel","brazil","maybe"]

randomIndex = random.randint(1,len(word)-1)
#word
guessWord = word[randomIndex]

dashes = []

for letter in guessWord:
    dashes.append("-")

for x in dashes:
    printYellow(x)