"""
Formatted String Output

Python offers multiple ways to format strings:
1. f-strings (Python 3.6+) - Most modern and readable
2. format() method - Versatile and powerful
3. % operator - Old-style formatting

Source: 00_review_and_more.docx - Section 5: Input and Output - Output
"""

name = "Alice"
age = 25

# ===== F-STRINGS (Recommended) =====
print("=== F-STRINGS (Python 3.6+) ===\n")

# Basic f-string
print(f"Hello, {name}. You are {age} years old.")

# F-strings with expressions
print(f"Next year, {name} will be {age + 1} years old.")

# F-strings with calculations
x = 10
y = 5
print(f"{x} + {y} = {x + y}")
print(f"{x} * {y} = {x * y}")

# F-strings with formatting
price = 19.99
print(f"Price: ${price:.2f}")  # 2 decimal places

# F-strings with method calls
text = "python"
print(f"Uppercase: {text.upper()}")
print(f"Capitalized: {text.capitalize()}")

# ===== FORMAT() METHOD =====
print("\n=== FORMAT() METHOD ===\n")

# Basic format
print("Hello, {}. You are {} years old.".format(name, age))

# Format with positional arguments
print("{0} is {1} years old. {0} loves programming.".format(name, age))

# Format with named arguments
print("{person} is {years} years old.".format(person=name, years=age))

# Format with number formatting
pi = 3.14159265359
print("Pi with 2 decimals: {:.2f}".format(pi))
print("Pi with 4 decimals: {:.4f}".format(pi))

# Format with width and alignment
print("Left aligned: '{:<10}'".format("text"))
print("Right aligned: '{:>10}'".format("text"))
print("Centered: '{:^10}'".format("text"))

# ===== % OPERATOR (Old Style) =====
print("\n=== % OPERATOR (Old Style) ===\n")

# String formatting with %s (string)
print("Hello, %s. You are %d years old." % (name, age))

# Integer formatting with %d
number = 42
print("The answer is %d." % number)

# Float formatting with %f
value = 3.14159
print("Pi: %.2f" % value)  # 2 decimal places

# Multiple values
print("Name: %s, Age: %d, Height: %.1f" % ("Bob", 30, 5.9))

# ===== COMPARISON OF METHODS =====
print("\n=== COMPARISON ===\n")

city = "New York"
temperature = 72.5

# All three methods producing same output:
print(f"Temperature in {city}: {temperature:.1f}°F")  # f-string
print("Temperature in {}: {:.1f}°F".format(city, temperature))  # format()
print("Temperature in %s: %.1f°F" % (city, temperature))  # % operator

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: User profile
username = "john_doe"
email = "john@example.com"
member_since = 2020

print(f"User Profile:")
print(f"  Username: {username}")
print(f"  Email: {email}")
print(f"  Member Since: {member_since}")

# Example 2: Price formatting
product = "Laptop"
original_price = 1299.99
discount = 0.15
final_price = original_price * (1 - discount)

print(f"\nProduct: {product}")
print(f"Original Price: ${original_price:.2f}")
print(f"Discount: {discount * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")
print(f"You save: ${original_price - final_price:.2f}")

# Example 3: Table formatting
print("\n=== Table Format ===")
print(f"{'Name':<10} {'Age':>5} {'City':<15}")
print("-" * 30)
print(f"{'Alice':<10} {25:>5} {'New York':<15}")
print(f"{'Bob':<10} {30:>5} {'Los Angeles':<15}")
print(f"{'Charlie':<10} {28:>5} {'Chicago':<15}")
