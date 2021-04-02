import math
import random
import os
import time
from colorama import init
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()


class Plane:

    def __init__(self, brand, model): #seats, engines, ceiling):
        self.brands=["Boeing","Airbus","Lockeed","Bombardier"]
        self.brand = self.checkBrand(brand.title())
        self.model = self.checkModel(model)
        # self.seats = seats
        # self.engines = engines
        # self.ceiling = ceiling
        

    def checkBrand(self, x):
        while x not in self.brands:
            print(f"{Fore.RED}Invalid value! {Fore.YELLOW}try again.{Style.RESET_ALL}")
            x = input("Brand: ").title()
        return x    

    def checkModel(self, x):
        while len(x)<3:
            print(f"{Fore.RED}Invalid value! {Fore.YELLOW}try again {Style.RESET_ALL}(At least 3 letters). ")
            x = input("Model: ")
        return x     

    def __str__(self):
        return f"{Fore.GREEN}plane brand:{Fore.YELLOW} {self.brand} {Fore.GREEN}plane model:{Fore.YELLOW} {self.model}{Style.RESET_ALL}"


brand = input("plane brand: ")   
model = input("plane model: ")   
plane = Plane(brand, model)
print(f"{plane}")