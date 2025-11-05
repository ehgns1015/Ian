"""
Functions - Basics

Functions are reusable blocks of code that perform a specific task.
They help organize code, avoid repetition, and make programs more modular.

Syntax:
def function_name(parameters):
    # function body
    return value

Source: 03_function.docx - Function Basics
"""

# Basic function definition and call
def greet():
    print("Hello, World!")

# Call the function
greet()

# Function with different messages
def say_goodbye():
    print("Goodbye!")

say_goodbye()

# Function that prints multiple lines
def show_menu():
    print("=== Menu ===")
    print("1. Start")
    print("2. Exit")

print("\n=== CALLING FUNCTIONS ===\n")
show_menu()

# Function with calculations
def calculate_sum():
    result = 10 + 20
    print(f"Sum: {result}")

print("\n=== FUNCTION WITH CALCULATIONS ===\n")
calculate_sum()

# Multiple function calls
def print_separator():
    print("-" * 40)

print("\n=== MULTIPLE CALLS ===\n")
print_separator()
print("Section 1")
print_separator()
print("Section 2")
print_separator()

# Function calling another function
def header():
    print("=" * 40)

def footer():
    print("=" * 40)

def display_message():
    header()
    print("Important Message")
    footer()

print("\n=== FUNCTION CALLING FUNCTIONS ===\n")
display_message()

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Display user info
def display_user_info():
    print("Username: john_doe")
    print("Email: john@example.com")
    print("Status: Active")

print("User Information:")
display_user_info()

# Example 2: Calculate area of square
def area_of_square():
    side = 5
    area = side * side
    print(f"Area of square with side {side}: {area}")

print("\nArea Calculation:")
area_of_square()

# Example 3: Print pattern
def print_triangle():
    for i in range(1, 6):
        print("*" * i)

print("\nTriangle Pattern:")
print_triangle()

# Example 4: Temperature converter
def celsius_to_fahrenheit_demo():
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

print("\nTemperature Conversion:")
celsius_to_fahrenheit_demo()

# Example 5: Greeting message
def morning_greeting():
    print("Good morning!")
    print("Have a great day!")

morning_greeting()

# Why use functions?
print("\n=== WHY USE FUNCTIONS? ===\n")
print("1. Code Reusability - Write once, use many times")
print("2. Organization - Group related code together")
print("3. Maintainability - Easy to update in one place")
print("4. Testing - Can test individual functions")
print("5. Readability - Makes code easier to understand")

# Demonstrating reusability
print("\n=== DEMONSTRATING REUSABILITY ===\n")

def print_stars():
    print("*" * 30)

# Using same function multiple times
print_stars()
print("Welcome Message")
print_stars()
print("Another Section")
print_stars()
