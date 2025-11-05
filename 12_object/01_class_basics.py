"""
Classes and Objects - Basics

Object-Oriented Programming (OOP) organizes code using classes and objects.
A class is a blueprint for creating objects.
An object is an instance of a class.

Source: Object.docx - Section 1: Defining Classes and Creating Objects
"""

# Basic class definition
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Creating objects (instances)
print("=== CREATING OBJECTS ===\n")

p1 = Person("Alice")
p1.greet()

p2 = Person("Bob")
p2.greet()

# Class with multiple attributes
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

print("\n=== MULTIPLE ATTRIBUTES ===\n")

car1 = Car("Toyota", "Camry", 2020)
car1.display_info()

car2 = Car("Honda", "Civic", 2021)
car2.display_info()

# Accessing attributes
print("\n=== ACCESSING ATTRIBUTES ===\n")

print(f"Car 1 brand: {car1.brand}")
print(f"Car 1 year: {car1.year}")

# Modifying attributes
car1.year = 2022
print(f"Updated year: {car1.year}")

# Class with methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

    def info(self):
        print(f"{self.name} is a {self.breed}")

print("\n=== METHODS ===\n")

dog = Dog("Buddy", "Golden Retriever")
dog.bark()
dog.info()

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Bank Account
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

account = BankAccount("12345", 1000)
print(f"Initial balance: ${account.get_balance()}")
account.deposit(500)
account.withdraw(200)

# Example 2: Student
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display(self):
        print(f"Student: {self.name}, ID: {self.student_id}, Grade: {self.grade}")

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"Grade updated to {self.grade}")

print("\nStudent Management:")
student = Student("Alice", "S001", "A")
student.display()
student.update_grade("A+")

# Example 3: Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

print("\nRectangle:")
rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

# Key concepts
print("\n=== KEY CONCEPTS ===\n")
print("Class: Blueprint for creating objects")
print("Object: Instance of a class")
print("__init__: Constructor method (initializes object)")
print("self: Reference to the current instance")
print("Attributes: Data stored in object (self.attribute)")
print("Methods: Functions defined in class")
