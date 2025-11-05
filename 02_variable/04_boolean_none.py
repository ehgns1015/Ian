"""
Boolean and None Types

Boolean represents True or False values.
None represents the absence of a value.

Source: 00_review_and_more.docx - Section 3: Basic Data Types - Boolean and None
"""

# Boolean values
is_valid = True
is_completed = False

print("Boolean True:", is_valid)
print("Boolean False:", is_completed)
print("Type:", type(is_valid))

# Boolean from comparisons
result = 10 > 5
print("\n10 > 5:", result)
print("Type:", type(result))

# Boolean from expressions
age = 25
is_adult = age >= 18
print("\nIs adult (age >= 18):", is_adult)

# Boolean in conditions
has_permission = True
if has_permission:
    print("Access granted")

# Truthy and Falsy values
# In Python, some values are considered False in boolean context:
# False, None, 0, 0.0, "", [], {}, ()

print("\nTruthy and Falsy values:")
print("bool(0):", bool(0))           # False
print("bool(1):", bool(1))           # True
print("bool(''):", bool(''))         # False (empty string)
print("bool('Hello'):", bool('Hello'))  # True
print("bool([]):", bool([]))         # False (empty list)
print("bool([1]):", bool([1]))       # True

# None type
result = None
print("\nNone value:", result)
print("Type:", type(result))

# None is used to represent absence of value
user_input = None  # No input yet
print("User input:", user_input)

# Checking for None
if result is None:
    print("Result is None")

# None is not the same as False or 0
print("\nNone == False:", None == False)  # False
print("None == 0:", None == 0)            # False
print("None is None:", None is None)      # True

# Common use case: default parameter or uninitialized variable
database_connection = None  # Not connected yet
print("Database connection:", database_connection)
