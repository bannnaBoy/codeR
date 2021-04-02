import math
import os
import random
import time
import colorama
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

cls()
init()

def rec():
    side1 = float(input("side 1: "))
    side2 = float(input("side 2: "))
    area = side1*side2
    print(f"The area of your rectangle ({side1}) by ({side2}) is {area} ")
    return{
        "shape":"rectangle",
        "side 1":side1,
        "side 2":side2,
        "area":area}

def tri():
    base = float(input("base: "))
    height = float(input("height: "))
    area = base*height/2.0
    print(f"The area of your triangle ({base}) by ({height}) is {area} ")
    return{
        "shape":"triangle",
        "base":base,
        "height":height,
        "area":area}

def cir():
    radius = float(input("radius: "))
    area = math.pi*math.pow(radius,2)
    print(f"The area of your circle (radius: {radius}) is {area} ")
    return{
        "shape":"circle",
        "radius":radius,
        "area":area}


functions = {"rectangle":rec, "triangle":tri, "circle":cir }

print("Choose the shape you want to calculate: ")

# count=1
# count = count+1
for index, k in enumerate(functions.keys()):
    print(f"{index+1}-{k}", end=" ")

print()
choice = input("your choice: ") 

if choice == "1":
    functions['rectangle']()

if choice == "2":
    functions['triangle']()

if choice == "3":
    functions['circle']()