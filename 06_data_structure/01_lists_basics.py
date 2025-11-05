"""
Lists - Basics

Lists are ordered, mutable collections that can store different data types.
Lists are created using square brackets [].

Source: 00_review_and_more.docx - Section 7: Lists
"""

# Creating lists
print("=== CREATING LISTS ===\n")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with items
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

# List with different data types
mixed_list = [1, "Hello", 3.14, True]
print(f"Mixed list: {mixed_list}")

# Using list() constructor
numbers = list([1, 2, 3, 4, 5])
print(f"Numbers: {numbers}")

# ===== ACCESSING ELEMENTS =====
print("\n=== ACCESSING ELEMENTS ===\n")

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
print(f"List: {fruits}")

# Indexing (positive)
first_fruit = fruits[0]
print(f"First fruit (index 0): {first_fruit}")

second_fruit = fruits[1]
print(f"Second fruit (index 1): {second_fruit}")

# Indexing (negative)
last_fruit = fruits[-1]
print(f"Last fruit (index -1): {last_fruit}")

second_last = fruits[-2]
print(f"Second last (index -2): {second_last}")

# ===== SLICING =====
print("\n=== SLICING ===\n")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Numbers: {numbers}")

# Basic slicing
subset = numbers[2:5]  # Elements from index 2 to 4
print(f"numbers[2:5]: {subset}")

# From beginning
subset = numbers[:4]  # First 4 elements
print(f"numbers[:4]: {subset}")

# To end
subset = numbers[5:]  # From index 5 to end
print(f"numbers[5:]: {subset}")

# Last N elements
subset = numbers[-3:]  # Last 3 elements
print(f"numbers[-3:]: {subset}")

# With step
subset = numbers[::2]  # Every 2nd element
print(f"numbers[::2]: {subset}")

# Reverse
reversed_list = numbers[::-1]
print(f"numbers[::-1]: {reversed_list}")

# ===== LIST LENGTH =====
print("\n=== LIST LENGTH ===\n")

fruits = ["apple", "banana", "cherry"]
length = len(fruits)
print(f"Fruits: {fruits}")
print(f"Length: {length}")

# ===== CHECKING MEMBERSHIP =====
print("\n=== CHECKING MEMBERSHIP ===\n")

fruits = ["apple", "banana", "cherry"]

# Check if item exists
if "banana" in fruits:
    print("Banana is in the list")

if "orange" not in fruits:
    print("Orange is not in the list")

# ===== ITERATING THROUGH LISTS =====
print("\n=== ITERATING ===\n")

colors = ["red", "blue", "green"]
print("Colors:")
for color in colors:
    print(f"  - {color}")

# With index
print("\nColors with index:")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Student grades
grades = [85, 90, 78, 92, 88]
print(f"Grades: {grades}")
print(f"Number of grades: {len(grades)}")
print(f"First grade: {grades[0]}")
print(f"Last grade: {grades[-1]}")

# Example 2: Shopping list
shopping_list = ["milk", "bread", "eggs", "butter"]
print(f"\nShopping list: {shopping_list}")
print(f"Items to buy: {len(shopping_list)}")

# Example 3: Temperature readings
temperatures = [72, 75, 68, 70, 73]
print(f"\nTemperatures: {temperatures}")
print(f"First 3 readings: {temperatures[:3]}")
print(f"Last 2 readings: {temperatures[-2:]}")
