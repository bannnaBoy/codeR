import math
import random
import os
from colorama import init
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

# class Car:
#     #constructor
#     def __init__(self,brand,model,color,engine,seats,hybrid):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.engine = engine
#         self.seats = seats
#         self.hybrid = hybrid
# my_brand = input("car brand: "+Fore.RED)
# my_model = input(Style.RESET_ALL+"car model: "+Fore.RED)
# my_color = input(Style.RESET_ALL+"car color: "+Fore.RED)
# my_engine = int(input(Style.RESET_ALL+"engine size: "+Fore.RED))
# my_seats = int(input(Style.RESET_ALL+"number of seats: "+Fore.RED))
# my_hybrid = input(Style.RESET_ALL+"hybrid? (t/f) "+Fore.RED)
# print(f"{Style.RESET_ALL}")

# my_Car = Car(my_brand,my_model,my_color,my_engine,my_seats,my_hybrid)

# print(f"{Style.RESET_ALL}{my_Car.brand}")


class student:
    def __init__(self,firstName,lastName,age,marks):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.marks = marks
        self.marksAverage = self.calculateAverage()

    def calculateAverage(self):
        total = 0
        for x in self.marks:
            total += x
        return total/len(self.marks)

    def studentDetails(self):
        print(f"{self.firstName}{self.lastName} {self.marksAverage}")

firstName = input("What is your first name? ")     
lastName = input("What is your last name? ")   
age = int(input("What is your age? "))
marks = []
while True:
    mark = int(input("mark: "))
    marks.append(mark)
    answer = input("More marks? (y/n) ")
    if answer.lower()=="n" or answer.lower()=="no":
        break
david = student(firstName,lastName,age,marks)    
david.studentDetails()