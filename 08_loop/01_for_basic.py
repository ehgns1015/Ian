"""
For Loop - Basic

The for loop iterates directly over sequences and iterable objects.
Unlike many other languages, Python's for loop is designed for iteration.

Source: 01_for_loop.docx - Section 1: Iterating Over Sequences
"""

# Iterating through a list
print("=== ITERATING THROUGH LIST ===\n")

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Iterating through a tuple
print("\n=== ITERATING THROUGH TUPLE ===\n")

colors = ('red', 'blue', 'green')
for color in colors:
    print(color)

# Iterating through a string
print("\n=== ITERATING THROUGH STRING ===\n")

for char in "Hello":
    print(char)

# Iterating with operations
print("\n=== WITH OPERATIONS ===\n")

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"{num} squared is {num ** 2}")

# Iterating with conditions
print("\n=== WITH CONDITIONS ===\n")

ages = [12, 25, 17, 30, 15]
for age in ages:
    if age >= 18:
        print(f"{age} - Adult")
    else:
        print(f"{age} - Minor")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Calculate sum
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# Example 2: Find maximum
scores = [85, 92, 78, 95, 88]
maximum = scores[0]
for score in scores:
    if score > maximum:
        maximum = score
print(f"\nScores: {scores}")
print(f"Maximum score: {maximum}")

# Example 3: Count items
fruits = ['apple', 'banana', 'apple', 'cherry', 'apple']
apple_count = 0
for fruit in fruits:
    if fruit == 'apple':
        apple_count += 1
print(f"\nFruits: {fruits}")
print(f"Apple count: {apple_count}")

# Example 4: Print with formatting
print("\n=== FORMATTED OUTPUT ===")
students = ['Alice', 'Bob', 'Charlie']
for student in students:
    print(f"Welcome, {student}!")

# Example 5: Multiple operations in loop
print("\n=== MULTIPLE OPERATIONS ===")
prices = [19.99, 29.99, 9.99]
tax_rate = 0.08

print("Price List with Tax:")
for price in prices:
    with_tax = price * (1 + tax_rate)
    print(f"${price:.2f} + tax = ${with_tax:.2f}")
