"""
For Loop with enumerate()

enumerate() adds a counter to an iterable and returns it as enumerate object.
This is useful when you need both the index and the value.

Source: 01_for_loop.docx - Section 3: The enumerate() Function
"""

# Basic enumerate
print("=== BASIC ENUMERATE ===\n")

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Enumerate with custom start
print("\n=== CUSTOM START INDEX ===\n")

colors = ['red', 'blue', 'green']
for index, color in enumerate(colors, start=1):
    print(f"Item #{index}: {color}")

# Enumerate with strings
print("\n=== ENUMERATE STRING ===\n")

text = "Python"
for index, char in enumerate(text):
    print(f"Position {index}: '{char}'")

# Enumerate with tuple
print("\n=== ENUMERATE TUPLE ===\n")

numbers = (10, 20, 30, 40)
for i, num in enumerate(numbers):
    print(f"[{i}] = {num}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Numbered list
print("=== TODO LIST ===")
tasks = ["Buy groceries", "Call mom", "Finish homework", "Clean room"]
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# Example 2: Find position of item
print("\n=== FIND POSITION ===")
names = ['Alice', 'Bob', 'Charlie', 'David']
search_name = 'Charlie'

for index, name in enumerate(names):
    if name == search_name:
        print(f"Found '{search_name}' at position {index}")
        break

# Example 3: Create numbered menu
print("\n=== MENU ===")
menu_items = ['Start Game', 'Load Game', 'Settings', 'Exit']
for i, item in enumerate(menu_items, start=1):
    print(f"{i}. {item}")

# Example 4: Track changes
print("\n=== PROCESSING WITH INDEX ===")
prices = [10.00, 20.00, 15.50, 30.00]
tax_rate = 0.08

for index, price in enumerate(prices):
    with_tax = price * (1 + tax_rate)
    print(f"Item {index + 1}: ${price:.2f} -> ${with_tax:.2f} (with tax)")

# Example 5: Modify list with position
print("\n=== MODIFY WITH INDEX ===")
numbers = [10, 20, 30, 40, 50]
print(f"Original: {numbers}")

# Double every other element
for index, num in enumerate(numbers):
    if index % 2 == 0:
        numbers[index] = num * 2

print(f"Modified: {numbers}")

# Example 6: Status report with completion
print("\n=== TASK STATUS ===")
tasks = ["Task A", "Task B", "Task C", "Task D"]
completed = [True, False, True, False]

for index, task in enumerate(tasks):
    status = "✓ Complete" if completed[index] else "✗ Pending"
    print(f"{index + 1}. {task}: {status}")

# Example 7: Generate CSV format
print("\n=== CSV FORMAT ===")
print("ID,Name,Score")
students = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for index, student in enumerate(students, start=1):
    print(f"{index},{student},{scores[index - 1]}")

# Example 8: Compare adjacent elements
print("\n=== COMPARE ADJACENT ===")
numbers = [1, 5, 3, 8, 2, 9]
print(f"Numbers: {numbers}")

for index, num in enumerate(numbers):
    if index < len(numbers) - 1:
        if num > numbers[index + 1]:
            print(f"Index {index}: {num} > {numbers[index + 1]}")

# Example 9: Build dictionary from list
print("\n=== BUILD DICTIONARY ===")
items = ['apple', 'banana', 'cherry']
item_dict = {}
for index, item in enumerate(items):
    item_dict[index] = item

print(f"Dictionary: {item_dict}")

# Example 10: Split list into chunks
print("\n=== EVERY 2ND ITEM ===")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_positions = []
odd_positions = []

for index, value in enumerate(data):
    if index % 2 == 0:
        even_positions.append(value)
    else:
        odd_positions.append(value)

print(f"Even index: {even_positions}")
print(f"Odd index: {odd_positions}")
