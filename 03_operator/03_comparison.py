"""
Comparison Operators

Comparison operators are used to compare two values.
They return a boolean value (True or False).

Operators: == (equal), != (not equal), > (greater than),
< (less than), >= (greater than or equal), <= (less than or equal)

Source: 00_review_and_more.docx - Section 4: Basic Operators - Comparison
"""

x = 5
y = 10

print(f"x = {x}, y = {y}\n")

# Equal to (==)
result = x == y
print(f"x == y: {result}")  # False

result = 5 == 5
print(f"5 == 5: {result}")  # True

# Not equal to (!=)
result = x != y
print(f"\nx != y: {result}")  # True

result = 5 != 5
print(f"5 != 5: {result}")  # False

# Greater than (>)
result = x > y
print(f"\nx > y: {result}")  # False

result = 10 > 5
print(f"10 > 5: {result}")  # True

# Less than (<)
result = x < y
print(f"\nx < y: {result}")  # True

result = 10 < 5
print(f"10 < 5: {result}")  # False

# Greater than or equal to (>=)
result = x >= y
print(f"\nx >= y: {result}")  # False

result = 10 >= 10
print(f"10 >= 10: {result}")  # True

result = 15 >= 10
print(f"15 >= 10: {result}")  # True

# Less than or equal to (<=)
result = x <= y
print(f"\nx <= y: {result}")  # True

result = 10 <= 10
print(f"10 <= 10: {result}")  # True

result = 5 <= 10
print(f"5 <= 10: {result}")  # True

# Comparing strings (lexicographical order)
print("\n=== String Comparison ===")
print("'apple' < 'banana':", 'apple' < 'banana')  # True
print("'zebra' > 'apple':", 'zebra' > 'apple')    # True
print("'hello' == 'hello':", 'hello' == 'hello')  # True
print("'Hello' == 'hello':", 'Hello' == 'hello')  # False (case-sensitive)

# Comparing different types
print("\n=== Comparing Different Types ===")
print("5 == 5.0:", 5 == 5.0)        # True (values are equal)
print("5 == '5':", 5 == '5')        # False (different types)
print("True == 1:", True == 1)       # True (True equals 1)
print("False == 0:", False == 0)     # True (False equals 0)

# Chaining comparisons
print("\n=== Chaining Comparisons ===")
age = 25
print(f"age = {age}")
print(f"18 <= age <= 65: {18 <= age <= 65}")  # True
print(f"1 < 2 < 3: {1 < 2 < 3}")              # True
print(f"1 < 3 < 2: {1 < 3 < 2}")              # False

# Practical example: Age verification
print("\n=== Practical Example ===")
user_age = 20
min_age = 18
max_age = 65

if user_age >= min_age:
    print(f"User is {user_age}, eligible (minimum age: {min_age})")
else:
    print(f"User is {user_age}, not eligible (minimum age: {min_age})")
