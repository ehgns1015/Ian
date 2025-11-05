"""
Input Function

The input() function allows user input from the keyboard.
It always returns a string, even if the user enters a number.

Source: 00_review_and_more.docx - Section 5: Input and Output - Input
"""

# Basic input - prompting user for text
name = input("Enter your name: ")
print("Hello, " + name)

# Input always returns a string
print("\n=== Input Returns String ===")
value = input("Enter a number: ")
print(f"You entered: {value}")
print(f"Type: {type(value)}")  # <class 'str'>

# Converting input to integer
print("\n=== Getting Numeric Input ===")
age = int(input("Enter your age: "))
print(f"You are {age} years old")
print(f"Type: {type(age)}")  # <class 'int'>

# Next year's age
next_year = age + 1
print(f"Next year you will be {next_year} years old")

# Converting input to float
print("\n=== Getting Decimal Input ===")
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters")
print(f"Type: {type(height)}")  # <class 'float'>

# Multiple inputs
print("\n=== Multiple Inputs ===")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Input in calculations
print("\n=== Input in Calculations ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
total = num1 + num2
print(f"{num1} + {num2} = {total}")

# Handling empty input
print("\n=== Empty Input ===")
response = input("Press Enter to continue (or type anything): ")
if response == "":
    print("You pressed Enter without typing anything")
else:
    print(f"You typed: {response}")

# Practical example: Simple calculator
print("\n=== Simple Calculator ===")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print(f"\nResults:")
print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")
print(f"{number1} / {number2} = {number1 / number2}")
