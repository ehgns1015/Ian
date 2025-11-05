"""
Import Basics

Modules are Python files containing functions, classes, and variables.
The import statement allows you to use code from other modules.

Source: Modules and Packages.docx - Import Basics
"""

# Importing built-in modules
import math

print("=== BASIC IMPORT ===\n")
print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"5 to the power of 3: {math.pow(5, 3)}")

# Importing multiple modules
import random
import datetime

print("\n=== MULTIPLE IMPORTS ===\n")
print(f"Random number: {random.randint(1, 100)}")
print(f"Current date: {datetime.date.today()}")

# Using module functions
print("\n=== USING MODULE FUNCTIONS ===\n")

# Math module
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")
print(f"Absolute of -10: {math.fabs(-10)}")

# Random module
colors = ['red', 'blue', 'green', 'yellow']
print(f"Random choice: {random.choice(colors)}")
print(f"Random float (0-1): {random.random()}")

# Datetime module
now = datetime.datetime.now()
print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Math calculations
def calculate_circle_area(radius):
    return math.pi * radius ** 2

radius = 5
area = calculate_circle_area(radius)
print(f"Circle area (radius {radius}): {area:.2f}")

# Example 2: Random selection
participants = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
winner = random.choice(participants)
print(f"\nLottery winner: {winner}")

# Example 3: Date formatting
today = datetime.date.today()
print(f"\nToday: {today}")
print(f"Day: {today.day}")
print(f"Month: {today.month}")
print(f"Year: {today.year}")

# Example 4: Random password generator
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(f"\nGenerated password: {generate_password()}")

# Commonly used built-in modules
print("\n=== COMMON BUILT-IN MODULES ===\n")
print("math - Mathematical functions")
print("random - Random number generation")
print("datetime - Date and time operations")
print("os - Operating system interface")
print("sys - System-specific parameters")
print("json - JSON encoding/decoding")
print("re - Regular expressions")
print("collections - Specialized container datatypes")
print("itertools - Functions for efficient looping")
print("string - Common string operations")
