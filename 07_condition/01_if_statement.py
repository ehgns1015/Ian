"""
If Statement

The if statement allows you to execute code conditionally.
Code inside the if block only runs if the condition is True.

Source: 00_review_and_more.docx - Section 11: Conditional Statements - if Statement
"""

# Basic if statement
age = 18

if age >= 18:
    print("You are an adult")

# Multiple statements in if block
score = 85

if score >= 60:
    print("Congratulations!")
    print("You passed the exam")
    print(f"Your score: {score}")

# If condition not met, block is skipped
temperature = 15

if temperature > 30:
    print("It's hot!")  # This won't print

print("This always prints")

# If with comparison operators
number = 10

if number > 0:
    print(f"{number} is positive")

if number < 20:
    print(f"{number} is less than 20")

if number == 10:
    print(f"{number} equals 10")

# If with logical operators
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")

# If with membership operators
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is available")

# If with string methods
username = "admin"

if username.lower() == "admin":
    print("Welcome, administrator!")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Password validation
password = "secret123"

if len(password) >= 8:
    print("Password length is valid")

# Example 2: Discount eligibility
purchase_amount = 150

if purchase_amount > 100:
    print("You qualify for a discount!")

# Example 3: Even number check
num = 8

if num % 2 == 0:
    print(f"{num} is even")

# Example 4: Temperature warning
temp = 38

if temp > 37.5:
    print("Warning: High temperature detected!")

# Example 5: Empty list check
items = []

if len(items) == 0:
    print("List is empty")

# Example 6: Username validation
username = "john_doe"

if username.isalnum():
    print("Username is valid (alphanumeric only)")
else:
    print("Username contains only letters and numbers")
