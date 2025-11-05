"""
Assignment Operators

Assignment operators are used to assign values to variables.
Compound assignment operators combine arithmetic with assignment.

Source: 00_review_and_more.docx - Section 4: Basic Operators - Assignment
"""

# Basic assignment
x = 5
print("x = 5")
print("x:", x)

# Addition assignment (+=)
x = 5
x += 3  # Equivalent to: x = x + 3
print("\nx = 5, then x += 3")
print("x:", x)  # 8

# Subtraction assignment (-=)
x = 10
x -= 2  # Equivalent to: x = x - 2
print("\nx = 10, then x -= 2")
print("x:", x)  # 8

# Multiplication assignment (*=)
x = 5
x *= 4  # Equivalent to: x = x * 4
print("\nx = 5, then x *= 4")
print("x:", x)  # 20

# Division assignment (/=)
x = 20
x /= 2  # Equivalent to: x = x / 2
print("\nx = 20, then x /= 2")
print("x:", x)  # 10.0

# Floor division assignment (//=)
x = 20
x //= 3  # Equivalent to: x = x // 3
print("\nx = 20, then x //= 3")
print("x:", x)  # 6

# Modulus assignment (%=)
x = 17
x %= 5  # Equivalent to: x = x % 5
print("\nx = 17, then x %= 5")
print("x:", x)  # 2

# Exponentiation assignment (**=)
x = 2
x **= 3  # Equivalent to: x = x ** 3
print("\nx = 2, then x **= 3")
print("x:", x)  # 8

# Multiple assignment in one line
a, b, c = 1, 2, 3
print("\na, b, c = 1, 2, 3")
print(f"a = {a}, b = {b}, c = {c}")

# Same value to multiple variables
a = b = c = 100
print("\na = b = c = 100")
print(f"a = {a}, b = {b}, c = {c}")

# Swapping values using multiple assignment
x, y = 10, 20
print(f"\nBefore swap: x = {x}, y = {y}")
x, y = y, x  # Swap values
print(f"After swap: x = {x}, y = {y}")

# Practical example: Accumulator pattern
total = 0
print("\nAccumulator example:")
print(f"Starting total: {total}")

total += 10
print(f"After adding 10: {total}")

total += 25
print(f"After adding 25: {total}")

total += 5
print(f"After adding 5: {total}")
