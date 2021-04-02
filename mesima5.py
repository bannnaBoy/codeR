import os
import random
import time
import colorama
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

grocery = {
    "milk": 5.40,
    "bread": 4.00,
    "cheese": 3.50,
    "oranges": 1.90,
    "cookies": 12.30,
    "snack": 2.60,
    "apple":3.30,
    "cola":6.40,
}

# for k, v in grocery.items():
#     print(f"product {k} = {v}")
# for k in grocery.keys():
#     print(f"product: {k}")    
# for v in grocery.values():
#     print(f"price: {v}")  
total=0   
totalFinal=0
for a in grocery.keys():
    print(f"product:{a}") 
while True:  
    choice = input("What do you want to buy? ")    
    if choice not in grocery.keys():
        print(f"{choice} is not in our stock")
    else:
        print(f"price of {choice} is {grocery[choice]}")    
        amount = int(input(f"How many {choice}'s do you want to buy? "))  
        total = grocery[choice]*amount
        print(f"for {amount} {choice}'s you need to pay {round(total,2)}")
        totalFinal=totalFinal+total
    answer = input(f"Do you want to continue? (y / n) ")   
    if answer.lower()!="y" and answer.lower() != "yes":
        break
print(f"your total is {round(totalFinal)}")    