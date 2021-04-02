import os
import colorama
from colorama import Fore, Back, Style, init
init()

def cls(): return os.system('cls')
cls()

#version1
#number 1 = int(input(number1))
#print("your number is"+str(number1))
#print(number1+number2)


number1 = int(input("choose the first number:"+Fore.RED))
print(f"{Style.RESET_ALL}you chose:{Fore.RED}{number1}")


number2 = int(input(Style.RESET_ALL+"choose the second number: "+Fore.YELLOW))
print(f"{Style.RESET_ALL}you chose:{Fore.YELLOW}{number2}")

print()

print(f"{Fore.GREEN}your total is: {number1+number2}{Style.RESET_ALL}")

print()

if number1<number2:
    print(f"Number 1 is {Fore.RED}SMALLER{Style.RESET_ALL} than number 2!")
if number1>number2:
    print(f"Number 1 is {Fore.GREEN}BIGGER{Style.RESET_ALL} than number 2!")
if number1==number2:
    print(f"Number 1 {Fore.MAGENTA}EQUALS{Style.RESET_ALL} to number 2!")