"""
Nested Loops

Nested loops are loops within loops.
The inner loop completes all iterations for each iteration of the outer loop.
Useful for working with multi-dimensional data or creating patterns.

Source: 01_for_loop.docx - Section 7: Nested For Loops
"""

# Basic nested loop
print("=== BASIC NESTED LOOP ===\n")

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Nested loop with lists
print("\n=== NESTED LOOP WITH LISTS ===\n")

colors = ['red', 'blue']
sizes = ['small', 'medium', 'large']

for color in colors:
    for size in sizes:
        print(f"{size} {color}")

# Multiplication table
print("\n=== MULTIPLICATION TABLE ===\n")

for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{i} x {j} = {product:2d}", end="  ")
    print()  # New line after each row

# Pattern printing
print("\n=== TRIANGLE PATTERN ===\n")

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # New line

# Number triangle
print("\n=== NUMBER TRIANGLE ===\n")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Print coordinates
print("=== COORDINATES ===")
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})", end=" ")
    print()

# Example 2: Matrix iteration
print("\n=== MATRIX ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix elements:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

print("\nMatrix with indices:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"[{i}][{j}]={matrix[i][j]}", end=" ")
    print()

# Example 3: Sum of matrix
print("\n=== MATRIX SUM ===")
total = 0
for row in matrix:
    for element in row:
        total += element
print(f"Sum of all elements: {total}")

# Example 4: Nested list comprehension equivalent
print("\n=== NESTED LIST COMPREHENSION ===")
coordinates = []
for x in range(3):
    for y in range(2):
        coordinates.append((x, y))

print(f"Coordinates: {coordinates}")

# Same thing with list comprehension
coords_comp = [(x, y) for x in range(3) for y in range(2)]
print(f"Using comprehension: {coords_comp}")

# Example 5: Generate all combinations
print("\n=== PRODUCT COMBINATIONS ===")
shirts = ['small', 'medium', 'large']
colors = ['red', 'blue', 'green']

print("Available combinations:")
count = 0
for shirt in shirts:
    for color in colors:
        count += 1
        print(f"{count}. {shirt} {color}")

# Example 6: Nested dictionary iteration
print("\n=== NESTED DICTIONARY ===")
students = {
    'class_a': ['Alice', 'Bob', 'Charlie'],
    'class_b': ['David', 'Eve', 'Frank']
}

for class_name, student_list in students.items():
    print(f"\n{class_name.upper()}:")
    for student in student_list:
        print(f"  - {student}")

# Example 7: Calendar grid
print("\n=== CALENDAR (4 weeks) ===")
print("Sun Mon Tue Wed Thu Fri Sat")
day = 1
for week in range(4):
    for weekday in range(7):
        if day <= 28:
            print(f"{day:3d}", end=" ")
            day += 1
    print()

# Example 8: Pyramid pattern
print("\n=== PYRAMID ===")
n = 5
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Example 9: Find pairs summing to target
print("\n=== FIND PAIRS ===")
numbers = [1, 2, 3, 4, 5]
target = 7

print(f"Numbers: {numbers}")
print(f"Target sum: {target}")
print("Pairs:")
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"  {numbers[i]} + {numbers[j]} = {target}")

# Example 10: Times table grid
print("\n=== TIMES TABLE (1-5) ===")
print("    ", end="")
for i in range(1, 6):
    print(f"{i:3d}", end=" ")
print()
print("   " + "-" * 20)

for i in range(1, 6):
    print(f"{i} | ", end="")
    for j in range(1, 6):
        print(f"{i*j:3d}", end=" ")
    print()
