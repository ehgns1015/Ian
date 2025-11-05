"""
Arithmetic Operators

Python supports standard mathematical operations:
+ (addition), - (subtraction), * (multiplication), / (division)
// (floor division), % (modulus), ** (exponentiation)

Source: 00_review_and_more.docx - Section 4: Basic Operators - Arithmetic
"""

# Addition
result = 5 + 3
print("5 + 3 =", result)  # 8

# Subtraction
result = 5 - 3
print("5 - 3 =", result)  # 2

# Multiplication
result = 5 * 3
print("5 * 3 =", result)  # 15

# Division (always returns float)
result = 5 / 2
print("5 / 2 =", result)  # 2.5

# Division with whole numbers still returns float
result = 10 / 2
print("10 / 2 =", result)  # 5.0 (float, not int)

# Floor division (returns integer, rounds down)
result = 5 // 2
print("5 // 2 =", result)  # 2

# Floor division with negative numbers
result = -5 // 2
print("-5 // 2 =", result)  # -3 (rounds down)

# Modulus (remainder)
result = 5 % 2
print("5 % 2 =", result)  # 1

# Modulus use case: checking even/odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Exponentiation (power)
result = 2 ** 3
print("2 ** 3 =", result)  # 8 (2 to the power of 3)

# Square root using exponentiation
result = 16 ** 0.5
print("16 ** 0.5 =", result)  # 4.0 (square root of 16)

# More complex expressions
result = (5 + 3) * 2 - 10 / 2
print("(5 + 3) * 2 - 10 / 2 =", result)  # 11.0

# Order of operations (PEMDAS)
result = 2 + 3 * 4  # Multiplication before addition
print("2 + 3 * 4 =", result)  # 14

result = (2 + 3) * 4  # Parentheses first
print("(2 + 3) * 4 =", result)  # 20

# Working with variables
x = 10
y = 3

print(f"\nWith x = {x} and y = {y}:")
print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")
print(f"x // y = {x // y}")
print(f"x % y = {x % y}")
print(f"x ** y = {x ** y}")
