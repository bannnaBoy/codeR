import os
import random
import time
import colorama
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

products = []
products.append(10)
print(products)

products = [1,2,3,"milk",True]
for i, p in enumerate(products):
    print(f"{i}=>{p}")

for p in products:
    print(p)

makolet = {"milk":4.30 , "coffee":1.10}
print(makolet)
words={"honda":"car" , "apple":"fruit"}
print(words["honda"])
print(words.keys())
print(words.values())

for k, v in words.items():
    print(f"{k} is a type of {v}")


count=len(words.keys())
print(count)
print(words.keys())
randomPlace = random.randint(0,count-1)
print([randomPlace])
words2=[]
for c in words.keys():
    words2.append(c)
myWord=words2[randomPlace]  
print(words[myWord])  
print(words2[randomPlace])