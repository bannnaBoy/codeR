import math
import random
import os
import time
from colorama import init
from colorama import Fore, Back, Style, init
init()
def cls(): return os.system('cls')
cls()

class Book:
    def __init__(self, title, author, available):
        self.title = title             #s
        self.author = author           #s
        self.available = available     #boolean

    def bookDetails(self):
        s=""
        if self.available == True:
            s="is"
        else:
            s="is not"    
        print(f"{self.title} by {self.author} {s} available")    

class User:
        def __init__(self, firstName, lastName, age):
            self.firstName = firstName           
            self.lastName = lastName         
            self.age = age

        def userDetails(self):    
            print(f"{self.firstName} {self.lastName}")  

class Library:
    def __init__(self, users, books):
        self.users = users     
        self.books = books 

    def allBooks(self):
        for book in self.books:
            book.bookDetails()
    def allUsers(self):
        for user in self.users:
            user.userDetails()   

books=[]
users=[]
while True:
    answer = input("Do you want to add a book to the library? (y/n) ")
    if answer.lower() == "y" or "yes":
        title = input("What is your book title? ")
        author = input("What is your book author? ")
        availability = input("Is your book available? (t/f) ")
        book = Book(title.title(), author.title(), availability.title())
        books.append(book)
    else:
        break
while True:
    answer = input("Do you want to add a user to the library? (y/n) ")
    if answer.lower() == "y" or "yes":
        firstName = input("What is your first name? ")
        lastName = input("What is your last name? ")
        age = int(input("What is your age? "))
        user = Book(firstName.title(), lastName.title(), age.title())
        books.append(book)
    else:
        break     