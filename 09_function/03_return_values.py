"""
Function Return Values

Functions can return values using the return statement.
This allows functions to produce results that can be stored or used elsewhere.

Source: 03_function.docx - Return Values
"""

# Function returning a value
def add(a, b):
    return a + b

print("=== BASIC RETURN ===\n")
result = add(10, 20)
print(f"Result: {result}")

# Using return value directly
print(f"5 + 7 = {add(5, 7)}")

# Function with multiple return statements
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

print("\n=== CONDITIONAL RETURN ===\n")
print(f"Score 95: Grade {get_grade(95)}")
print(f"Score 85: Grade {get_grade(85)}")

# Function returning multiple values (tuple)
def get_user_info():
    return "Alice", 25, "alice@example.com"

print("\n=== RETURNING MULTIPLE VALUES ===\n")
name, age, email = get_user_info()
print(f"Name: {name}, Age: {age}, Email: {email}")

# Function returning different types
def square(num):
    return num ** 2

def is_even(num):
    return num % 2 == 0

print("\n=== DIFFERENT RETURN TYPES ===\n")
print(f"Square of 5: {square(5)}")
print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Calculate area
def calculate_rectangle_area(length, width):
    return length * width

area = calculate_rectangle_area(5, 10)
print(f"Rectangle area: {area}")

# Example 2: Temperature conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_f = celsius_to_fahrenheit(25)
print(f"25°C = {temp_f}°F")

# Example 3: Find maximum
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

maximum = find_max(10, 25, 15)
print(f"Maximum of 10, 25, 15: {maximum}")

# Example 4: String manipulation
def get_initials(first_name, last_name):
    return f"{first_name[0]}.{last_name[0]}."

initials = get_initials("John", "Doe")
print(f"Initials: {initials}")

# Example 5: Calculate discount
def calculate_final_price(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount

final = calculate_final_price(100, 20)
print(f"Final price after 20% discount: ${final}")

# Example 6: Validate input
def is_valid_age(age):
    return age >= 0 and age <= 120

print(f"\nIs 25 valid age? {is_valid_age(25)}")
print(f"Is -5 valid age? {is_valid_age(-5)}")

# Example 7: List operations
def get_sum_and_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg

nums = [10, 20, 30, 40, 50]
sum_val, avg_val = get_sum_and_average(nums)
print(f"\nNumbers: {nums}")
print(f"Sum: {sum_val}, Average: {avg_val}")

# Example 8: Dictionary creation
def create_user_dict(name, age, city):
    return {'name': name, 'age': age, 'city': city}

user = create_user_dict("Alice", 25, "New York")
print(f"\nUser: {user}")

# Example 9: Using return values in expressions
def multiply(a, b):
    return a * b

result = multiply(5, 10) + multiply(3, 4)
print(f"\n(5*10) + (3*4) = {result}")

# Example 10: None return (default)
def print_message(msg):
    print(msg)
    # No explicit return - returns None

result = print_message("Hello")
print(f"Return value: {result}")
