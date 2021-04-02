import random
import os

from colorama import init
from colorama import Fore, Back, Style, init

init()


def cls(): return os.system('cls')

cls()


def printRed(s):
    print(f"{Fore.RED}{s}{Style.RESET_ALL}")


def printYellow(s):
    print(f"{Fore.YELLOW}{s}{Style.RESET_ALL}", end="")

def inputBlue(s):
    return f"{s}{Fore.BLUE}"


countries = ["germany", "canada", "italy", "ecuador", "argentina", "greece", "israel", "england", "japan", "korea",
             "australia",
             "brazil", "portugal", "egypt", "kenya", "holland", "peru", "poland", "france", "sweden"]

randomIndex = random.randint(0, len(countries)-1 ) #length

secretCountry = countries[randomIndex]

dashes =[]

for x in secretCountry:
    dashes.append(" - ")

# for x in secretCountry:
#     print(f" {x} ", end="")

print()



for dash in dashes:
    printYellow(dash)

letter=""
while " - " in dashes:
    print()
    letter = input("type your  letter: ")
    if letter in secretCountry:
        for a in range():
            if secretCountry[a]==letter:
                dashes[a]=letter+" "
    for dash in dashes:
        printYellow(dash)

print("AMAZING!!!")
