"""
Membership and Identity Operators

Membership operators: in, not in
- Test if a value is present in a sequence

Identity operators: is, is not
- Test if two variables refer to the same object

Source: 00_review_and_more.docx - Section 4: Membership and Identity Operators
"""

# ===== MEMBERSHIP OPERATORS =====

print("=== MEMBERSHIP OPERATORS ===\n")

# 'in' operator with list
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

result = "banana" in fruits
print(f"'banana' in fruits: {result}")  # True

result = "orange" in fruits
print(f"'orange' in fruits: {result}")  # False

# 'not in' operator
result = "orange" not in fruits
print(f"'orange' not in fruits: {result}")  # True

result = "apple" not in fruits
print(f"'apple' not in fruits: {result}")  # False

# 'in' with strings (substring check)
print("\n=== Membership with Strings ===")
text = "Hello, World!"
print(f"Text: '{text}'")

result = "World" in text
print(f"'World' in text: {result}")  # True

result = "Python" in text
print(f"'Python' in text: {result}")  # False

# 'in' with dictionaries (checks keys)
print("\n=== Membership with Dictionaries ===")
person = {"name": "John", "age": 30, "city": "New York"}
print(f"Person: {person}")

result = "name" in person
print(f"'name' in person: {result}")  # True

result = "John" in person
print(f"'John' in person: {result}")  # False (value, not key)

# 'in' with tuples
print("\n=== Membership with Tuples ===")
numbers = (1, 2, 3, 4, 5)
print(f"Numbers: {numbers}")

result = 3 in numbers
print(f"3 in numbers: {result}")  # True

# ===== IDENTITY OPERATORS =====

print("\n\n=== IDENTITY OPERATORS ===\n")

# 'is' operator - checks if variables refer to the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

result = x is z
print(f"\nx is z: {result}")  # True (same object)

result = x is y
print(f"x is y: {result}")  # False (different objects, same content)

result = x == y
print(f"x == y: {result}")  # True (same content)

# 'is not' operator
result = x is not y
print(f"\nx is not y: {result}")  # True

# Identity with immutable objects (integers)
print("\n=== Identity with Small Integers ===")
a = 256
b = 256
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # True (Python caches small integers)

a = 257
b = 257
print(f"\na = {a}, b = {b}")
print(f"a is b: {a is b}")  # May be False (larger integers)

# Identity with None
print("\n=== Identity with None ===")
value = None
print(f"value = {value}")
print(f"value is None: {value is None}")  # True (recommended)
print(f"value == None: {value == None}")  # True (but 'is' is preferred)

# Practical example
print("\n=== Practical Example ===")
database_connection = None

if database_connection is None:
    print("Database not connected")
else:
    print("Database connected")

# Checking object identity
print("\n=== Object Identity Check ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 id: {id(list1)}")
print(f"list2 id: {id(list2)}")
print(f"list3 id: {id(list3)}")

print(f"\nlist1 is list2: {list1 is list2}")  # False (different objects)
print(f"list1 is list3: {list1 is list3}")    # True (same object)
print(f"list1 == list2: {list1 == list2}")    # True (same content)
