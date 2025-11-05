"""
Tuples

Tuples are ordered, immutable collections that can store different data types.
Once created, tuples cannot be modified (immutable).
Tuples are created using parentheses ().

Source: 00_review_and_more.docx - Section 8: Tuples
"""

# ===== CREATING TUPLES =====
print("=== CREATING TUPLES ===\n")

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with items
fruits = ("apple", "banana", "cherry")
print(f"Fruits: {fruits}")

# Mixed data types
mixed_tuple = (1, "Hello", 3.14, True)
print(f"Mixed tuple: {mixed_tuple}")

# Single-item tuple (note the comma!)
single_item = ("apple",)  # Comma is required
print(f"Single item: {single_item}")
print(f"Type: {type(single_item)}")

# Without comma, it's not a tuple
not_tuple = ("apple")  # This is just a string
print(f"Not a tuple: {not_tuple}, Type: {type(not_tuple)}")

# Using tuple() constructor
numbers = tuple([1, 2, 3, 4, 5])
print(f"\nNumbers: {numbers}")

# ===== ACCESSING ELEMENTS =====
print("\n=== ACCESSING ELEMENTS ===\n")

colors = ("red", "blue", "green", "yellow", "purple")
print(f"Colors: {colors}")

# Positive indexing
first = colors[0]
print(f"First color (index 0): {first}")

# Negative indexing
last = colors[-1]
print(f"Last color (index -1): {last}")

# Slicing
subset = colors[1:4]
print(f"colors[1:4]: {subset}")

# ===== IMMUTABILITY =====
print("\n=== IMMUTABILITY ===\n")

numbers = (1, 2, 3, 4, 5)
print(f"Original tuple: {numbers}")

# This would cause an error:
# numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment

print("Tuples cannot be modified after creation")

# ===== TUPLE OPERATIONS =====
print("\n=== TUPLE OPERATIONS ===\n")

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")
print(f"Combined: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"\ntuple1 * 3: {repeated}")

# Length
length = len(tuple1)
print(f"\nLength of {tuple1}: {length}")

# ===== TUPLE METHODS =====
print("\n=== TUPLE METHODS ===\n")

numbers = (3, 1, 4, 1, 5, 9, 2, 1)
print(f"Numbers: {numbers}")

# count() - Count occurrences
count = numbers.count(1)
print(f"Count of 1: {count}")

# index() - Find first occurrence
index = numbers.index(5)
print(f"Index of 5: {index}")

# ===== MEMBERSHIP =====
print("\n=== MEMBERSHIP ===\n")

fruits = ("apple", "banana", "cherry")

if "banana" in fruits:
    print("Banana is in the tuple")

if "orange" not in fruits:
    print("Orange is not in the tuple")

# ===== ITERATING =====
print("\n=== ITERATING ===\n")

colors = ("red", "blue", "green")
print("Colors:")
for color in colors:
    print(f"  - {color}")

# With index
print("\nColors with index:")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# ===== TUPLE UNPACKING =====
print("\n=== TUPLE UNPACKING ===\n")

# Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"Coordinates: {coordinates}")
print(f"x = {x}, y = {y}")

# Multiple values
person = ("John", 30, "New York")
name, age, city = person
print(f"\nPerson tuple: {person}")
print(f"Name: {name}, Age: {age}, City: {city}")

# Swapping variables using tuples
a, b = 5, 10
print(f"\nBefore swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# ===== WHY USE TUPLES? =====
print("\n=== WHY USE TUPLES? ===\n")

print("1. Faster than lists")
print("2. Protect data that shouldn't change")
print("3. Can be used as dictionary keys (unlike lists)")
print("4. Good for returning multiple values from functions")

# Example: Function returning tuple
def get_user_info():
    return ("Alice", 25, "alice@example.com")

user_data = get_user_info()
print(f"\nUser data: {user_data}")
name, age, email = get_user_info()
print(f"Unpacked: {name}, {age}, {email}")

# ===== NESTED TUPLES =====
print("\n=== NESTED TUPLES ===\n")

nested = ((1, 2), (3, 4), (5, 6))
print(f"Nested tuple: {nested}")
print(f"First tuple: {nested[0]}")
print(f"First element of first tuple: {nested[0][0]}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Days of week (fixed data)
DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(f"Days of week: {DAYS}")
print(f"First day: {DAYS[0]}")
print(f"Weekend: {DAYS[5:]}")

# Example 2: RGB colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
print(f"\nRed: {red}")
print(f"Green: {green}")
print(f"Blue: {blue}")

# Example 3: Coordinates
point = (10, 20, 30)  # x, y, z
x, y, z = point
print(f"\nPoint: {point}")
print(f"X: {x}, Y: {y}, Z: {z}")

# Example 4: Database record (immutable)
user_record = (101, "john_doe", "john@example.com", "2024-01-15")
user_id, username, email, created = user_record
print(f"\nUser record: {user_record}")
print(f"User ID: {user_id}")
print(f"Username: {username}")
