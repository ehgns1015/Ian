"""
For Loop with range()

The range() function generates a sequence of numbers.
It's commonly used for iterating a specific number of times.

Syntax:
- range(stop): 0 to stop-1
- range(start, stop): start to stop-1
- range(start, stop, step): start to stop-1 with step

Source: 01_for_loop.docx - Section 2: Using the range() Function
"""

# Basic range (0 to n-1)
print("=== BASIC RANGE ===\n")

for i in range(5):
    print(i)

# Range with start and end
print("\n=== RANGE WITH START AND END ===\n")

for i in range(2, 6):
    print(i)

# Range with step
print("\n=== RANGE WITH STEP ===\n")

for i in range(1, 10, 2):
    print(i)

# Reverse range (counting down)
print("\n=== REVERSE RANGE ===\n")

for i in range(10, 0, -1):
    print(i)

# Negative range
print("\n=== NEGATIVE RANGE ===\n")

for i in range(-5, 1):
    print(i)

# Range with larger step
print("\n=== RANGE WITH STEP 3 ===\n")

for i in range(0, 20, 3):
    print(i)

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Calculate sum of even numbers
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(f"Sum of even numbers (1-100): {total}")

# Example 2: Multiplication table
print("\n=== MULTIPLICATION TABLE (5) ===")
for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")

# Example 3: Countdown
print("\n=== COUNTDOWN ===")
for i in range(5, 0, -1):
    print(f"{i}...")
print("Go!")

# Example 4: Print squares
print("\n=== SQUARES ===")
for i in range(1, 6):
    print(f"{i}^2 = {i**2}")

# Example 5: Generate list using range
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(f"\nSquares (1-10): {squares}")

# Example 6: Print pattern
print("\n=== PATTERN ===")
for i in range(1, 6):
    print("*" * i)

# Example 7: Temperature conversion
print("\n=== CELSIUS TO FAHRENHEIT ===")
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

# Example 8: Access list by index
print("\n=== ACCESS BY INDEX ===")
fruits = ['apple', 'banana', 'cherry', 'date']
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# Example 9: Factorial
print("\n=== FACTORIAL ===")
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# Example 10: Powers of 2
print("\n=== POWERS OF 2 ===")
for i in range(0, 11):
    print(f"2^{i} = {2**i}")
