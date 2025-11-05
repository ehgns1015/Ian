"""
Try-Except - Basic Error Handling

The try-except block allows you to handle errors gracefully.
Code in the try block is executed, and if an error occurs,
the except block handles it.

Source: Error Handling.docx - Basic Try-Except
"""

# Basic try-except
print("=== BASIC TRY-EXCEPT ===\n")

try:
    result = 10 / 0
except:
    print("An error occurred!")

print("Program continues...")

# Specific exception handling
print("\n=== SPECIFIC EXCEPTION ===\n")

try:
    number = int("abc")
except ValueError:
    print("ValueError: Cannot convert string to integer")

# Multiple operations in try block
print("\n=== MULTIPLE OPERATIONS ===\n")

try:
    x = 10
    y = 0
    result = x / y
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Accessing error message
print("\n=== ERROR MESSAGE ===\n")

try:
    value = int("not a number")
except ValueError as e:
    print(f"Error occurred: {e}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Safe division
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

# Example 2: File reading
print("\n=== FILE READING ===")

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")

# Example 3: List index
print("\n=== LIST INDEX ===")

numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Index out of range")

# Example 4: Dictionary key
print("\n=== DICTIONARY KEY ===")

person = {"name": "Alice", "age": 25}
try:
    email = person["email"]
except KeyError:
    print("Key 'email' not found")

# Example 5: Type conversion
print("\n=== TYPE CONVERSION ===")

user_input = "abc"
try:
    age = int(user_input)
    print(f"Age: {age}")
except ValueError:
    print(f"'{user_input}' is not a valid number")

# Example 6: Safe input processing
print("\n=== SAFE INPUT PROCESSING ===")

inputs = ["10", "20", "abc", "30"]
total = 0

for inp in inputs:
    try:
        total += int(inp)
        print(f"Added {inp}, Total: {total}")
    except ValueError:
        print(f"Skipped invalid input: {inp}")

print(f"Final total: {total}")

# Common exceptions
print("\n=== COMMON EXCEPTIONS ===\n")
print("- ValueError: Invalid value for operation")
print("- TypeError: Wrong type for operation")
print("- ZeroDivisionError: Division by zero")
print("- FileNotFoundError: File doesn't exist")
print("- IndexError: List index out of range")
print("- KeyError: Dictionary key not found")
print("- AttributeError: Object has no attribute")
