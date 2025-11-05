"""
Multiple Exception Handling

You can handle different types of exceptions separately
using multiple except blocks or catching multiple exceptions together.

Source: Error Handling.docx - Multiple Exceptions
"""

# Multiple except blocks
print("=== MULTIPLE EXCEPT BLOCKS ===\n")

def process_data(data, index):
    try:
        value = int(data[index])
        result = 100 / value
        return result
    except IndexError:
        print("Error: Index out of range")
    except ValueError:
        print("Error: Cannot convert to integer")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

# Test different error scenarios
data = ["10", "0", "abc"]
print(f"Data: {data}\n")

print("Processing index 0:")
process_data(data, 0)

print("\nProcessing index 1:")
process_data(data, 1)

print("\nProcessing index 2:")
process_data(data, 2)

print("\nProcessing index 5:")
process_data(data, 5)

# Catching multiple exceptions together
print("\n\n=== CATCHING MULTIPLE EXCEPTIONS ===\n")

def safe_operation(a, b, operation):
    try:
        if operation == "divide":
            return a / b
        elif operation == "index":
            return a[b]
    except (ZeroDivisionError, IndexError, TypeError) as e:
        print(f"Operation failed: {type(e).__name__}")
        return None

print(safe_operation(10, 0, "divide"))
print(safe_operation([1, 2, 3], 10, "index"))

# Generic exception handler
print("\n=== GENERIC EXCEPTION HANDLER ===\n")

def risky_function(x):
    try:
        result = int(x) / len(x)
        return result
    except ValueError:
        print("ValueError occurred")
    except TypeError:
        print("TypeError occurred")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")

risky_function("abc")
risky_function(123)
risky_function([])

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Calculator with error handling
def calculator(num1, num2, operation):
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2
        else:
            raise ValueError("Invalid operation")
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid number type"
    except ValueError as e:
        return f"Error: {e}"

print("Calculator:")
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 / 0 = {calculator(10, 0, '/')}")
print(f"10 % 5 = {calculator(10, 5, '%')}")

# Example 2: Data validator
print("\n=== DATA VALIDATOR ===")

def validate_user_data(name, age, email):
    errors = []

    try:
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        if len(name) < 2:
            raise ValueError("Name too short")
    except (TypeError, ValueError) as e:
        errors.append(f"Name error: {e}")

    try:
        age_int = int(age)
        if age_int < 0 or age_int > 120:
            raise ValueError("Age out of range")
    except (ValueError, TypeError) as e:
        errors.append(f"Age error: {e}")

    try:
        if "@" not in email:
            raise ValueError("Invalid email format")
    except (ValueError, TypeError) as e:
        errors.append(f"Email error: {e}")

    return errors

# Test validation
test_data = [
    ("Alice", "25", "alice@example.com"),
    ("A", "25", "alice@example.com"),
    ("Bob", "abc", "bob@example.com"),
    ("Charlie", "30", "invalid-email")
]

for name, age, email in test_data:
    errors = validate_user_data(name, age, email)
    if errors:
        print(f"\nValidating {name}:")
        for error in errors:
            print(f"  - {error}")
    else:
        print(f"\n{name}: All valid ✓")

# Example 3: File operations with multiple error handling
print("\n=== FILE OPERATIONS ===")

def read_file_safe(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found")
    except PermissionError:
        print(f"No permission to read '{filename}'")
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
    return None

read_file_safe("nonexistent.txt")

# Exception hierarchy
print("\n=== EXCEPTION HIERARCHY ===\n")
print("Specific exceptions should be caught before generic ones:")
print("1. Specific: ValueError, TypeError, etc.")
print("2. General: Exception")
print("3. Catch-all: except (without type)")
print("\nOrder matters - Python checks from top to bottom!")
