import os
import random
import colorama
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

# print("Random number generator")
# print()
# low = int(input("Type your low range here: "))
# heigh = int(input("Type your heigh range here: "))

answer="yes"
while answer.lower() =="yes":
    print()
    times = int(input("How many random numbers do you want? "+Fore.RED))
    print()
    print(f"{Style.RESET_ALL}You want {Fore.RED}{times}{Style.RESET_ALL} random numbers")
    print()
    for x in range(times):
        number = random.randint(1,100)
        print(f"number {x+1}: {number}")
        if number % 2==0:
            print(f"{number} is an {Fore.GREEN}even{Style.RESET_ALL} number")
            print()
        else:    
            print(f"{number} is an {Fore.RED}odd{Style.RESET_ALL} number")
        print()
    answer=input("Do you  want to return to start? ")
# print(f"Your random number is: {random.randint(low,heigh)}")