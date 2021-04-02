import os
import colorama
from colorama import Fore, Back, Style, init
init()

def cls(): return os.system('cls')
cls()

number1 = int(input("choose the first number:"+Fore.RED))

number2 = int(input(Style.RESET_ALL+"choose the second number: "+Fore.RED))

number3 = int(input(Style.RESET_ALL+"choose the third number: "+Fore.RED))

print(f"{Style.RESET_ALL}Your multiplication answer is: {Fore.YELLOW}{number1*number2*number3}{Style.RESET_ALL}")

name = (input("type your name here: "+Fore.GREEN))
sirname = (input(Style.RESET_ALL+"type your sirname here: "+Fore.GREEN))

banana = (" ")

print(f"{Style.RESET_ALL}Your name is: {Fore.BLUE}{name+banana+sirname}")