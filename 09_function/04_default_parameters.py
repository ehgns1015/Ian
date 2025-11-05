"""
Default Parameters

Functions can have default parameter values.
If no argument is provided, the default value is used.

Syntax:
def function_name(param1, param2=default_value):
    # function body

Source: 03_function.docx - Default Parameters
"""

# Function with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

print("=== DEFAULT PARAMETERS ===\n")
greet("Alice")  # Uses provided argument
greet()  # Uses default value

# Multiple default parameters
def create_profile(name, age=18, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

print("\n=== MULTIPLE DEFAULTS ===\n")
create_profile("Alice", 25, "New York")
create_profile("Bob", 30)
create_profile("Charlie")

# Default with calculation
def calculate_price(base_price, tax_rate=0.08):
    total = base_price * (1 + tax_rate)
    return total

print("\n=== DEFAULT IN CALCULATION ===\n")
print(f"Price with default tax: ${calculate_price(100):.2f}")
print(f"Price with custom tax: ${calculate_price(100, 0.10):.2f}")

# Keyword arguments with defaults
def send_email(recipient, subject="No Subject", body=""):
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print()

print("=== KEYWORD ARGUMENTS ===\n")
send_email("alice@example.com", "Meeting", "See you at 3pm")
send_email("bob@example.com", body="Quick message")
send_email("charlie@example.com")

# Practical examples
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: Power function
def power(base, exponent=2):
    return base ** exponent

print(f"5^2 (default): {power(5)}")
print(f"5^3: {power(5, 3)}")
print(f"2^10: {power(2, 10)}")

# Example 2: Print separator
def print_separator(char="-", length=40):
    print(char * length)

print("\nSeparators:")
print_separator()
print_separator("=")
print_separator("*", 30)

# Example 3: Create user
def create_user(username, role="user", active=True):
    return {
        'username': username,
        'role': role,
        'active': active
    }

admin = create_user("alice", "admin")
user = create_user("bob")
inactive = create_user("charlie", active=False)

print("\nUsers:")
print(admin)
print(user)
print(inactive)

# Example 4: Format currency
def format_currency(amount, symbol="$", decimals=2):
    return f"{symbol}{amount:.{decimals}f}"

print("\nCurrency Formatting:")
print(format_currency(99.5))
print(format_currency(99.5, "€"))
print(format_currency(99.567, "$", 3))

# Example 5: Log message
def log(message, level="INFO", timestamp=True):
    prefix = "[LOG] " if timestamp else ""
    print(f"{prefix}[{level}] {message}")

print("\nLog Messages:")
log("Application started")
log("Error occurred", "ERROR")
log("Debug info", "DEBUG", False)

# Example 6: Calculate discount
def apply_discount(price, discount=10, show_details=True):
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    if show_details:
        print(f"Original: ${price}")
        print(f"Discount: {discount}%")
        print(f"You save: ${discount_amount}")
        print(f"Final: ${final_price}")
    return final_price

print("\nDiscount Calculation:")
apply_discount(100)
print()
apply_discount(200, 20)
print()
result = apply_discount(150, 15, False)
print(f"Silent calculation result: ${result}")

# Example 7: Repeat string
def repeat(text, times=3, separator=" "):
    return separator.join([text] * times)

print("\nRepeat Operations:")
print(repeat("Hello"))
print(repeat("Python", 5))
print(repeat("Hi", 4, ", "))

# Example 8: Validate password
def validate_password(password, min_length=8, require_digit=True):
    if len(password) < min_length:
        return False, f"Too short (min {min_length})"

    if require_digit and not any(char.isdigit() for char in password):
        return False, "Must contain digit"

    return True, "Valid"

print("\nPassword Validation:")
passwords = ["short", "longpassword", "pass123"]
for pwd in passwords:
    valid, msg = validate_password(pwd)
    print(f"'{pwd}': {msg}")
