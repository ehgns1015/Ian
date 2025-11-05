"""
Function Parameters

Parameters (or arguments) allow you to pass data into functions.
This makes functions more flexible and reusable.

Syntax:
def function_name(parameter1, parameter2):
    # use parameters

Source: 03_function.docx - Function Parameters
"""

# Function with single parameter
def greet(name):
    print(f"Hello, {name}!")

print("=== SINGLE PARAMETER ===\n")
greet("Alice")
greet("Bob")
greet("Charlie")

# Function with multiple parameters
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

print("\n=== MULTIPLE PARAMETERS ===\n")
introduce("Alice", 25)
introduce("Bob", 30)

# Function with calculation
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

print("\n=== PARAMETERS IN CALCULATIONS ===\n")
add_numbers(10, 20)
add_numbers(5, 15)

# Function with three parameters
def calculate_area(length, width, height):
    volume = length * width * height
    print(f"Volume: {length} x {width} x {height} = {volume}")

print("\n=== THREE PARAMETERS ===\n")
calculate_area(3, 4, 5)

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Personalized greeting
def greet_user(name, time_of_day):
    print(f"Good {time_of_day}, {name}!")

greet_user("Alice", "morning")
greet_user("Bob", "evening")

# Example 2: Calculate rectangle area
def rectangle_area(length, width):
    area = length * width
    print(f"Rectangle: {length} x {width} = {area} sq units")

print("\nRectangle Areas:")
rectangle_area(5, 10)
rectangle_area(7, 3)

# Example 3: Display product info
def show_product(name, price, quantity):
    total = price * quantity
    print(f"Product: {name}")
    print(f"Price: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total}")
    print()

print("Product Information:")
show_product("Laptop", 999.99, 2)
show_product("Mouse", 29.99, 5)

# Example 4: Temperature conversion
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

print("Temperature Conversions:")
celsius_to_fahrenheit(0)
celsius_to_fahrenheit(25)
celsius_to_fahrenheit(100)

# Example 5: Create email address
def create_email(first_name, last_name, domain):
    email = f"{first_name}.{last_name}@{domain}"
    print(f"Email: {email}")

print("\nEmail Addresses:")
create_email("john", "doe", "example.com")
create_email("jane", "smith", "company.org")

# Example 6: Calculate discount
def apply_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    print(f"Original: ${price}")
    print(f"Discount: {discount_percent}% (${discount_amount})")
    print(f"Final price: ${final_price}")
    print()

print("Discount Calculations:")
apply_discount(100, 10)
apply_discount(250, 20)

# Example 7: Print pattern with parameters
def print_pattern(character, count):
    print(character * count)

print("Patterns:")
print_pattern("*", 10)
print_pattern("-", 20)
print_pattern("=", 15)

# Example 8: Calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(f"Weight: {weight}kg, Height: {height}m")
    print(f"BMI: {bmi:.2f}")

print("\nBMI Calculations:")
calculate_bmi(70, 1.75)
calculate_bmi(85, 1.80)

# Example 9: Display user profile
def show_profile(username, email, age, city):
    print(f"--- Profile ---")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print()

show_profile("alice123", "alice@email.com", 25, "New York")
show_profile("bob456", "bob@email.com", 30, "Los Angeles")

# Example 10: Math operations
def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2
    else:
        result = None

    if result is not None:
        print(f"{num1} {operation} {num2} = {result}")

print("Math Operations:")
perform_operation(10, 5, "add")
perform_operation(10, 5, "subtract")
perform_operation(10, 5, "multiply")
perform_operation(10, 5, "divide")

# Parameter naming
print("\n=== PARAMETER NAMING ===\n")
print("Good parameter names:")
print("- Descriptive: calculate_area(length, width)")
print("- Clear intent: send_email(recipient, subject, body)")
print("- Consistent: get_user_info(user_id)")
