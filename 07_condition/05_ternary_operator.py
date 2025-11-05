"""
Ternary Operator (Conditional Expression)

The ternary operator is a concise way to write simple if-else statements.
Syntax: value_if_true if condition else value_if_false

Source: 00_review_and_more.docx - Section 11: Conditional Statements - Conditional Expressions
"""

# Basic ternary operator
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age: {age}, Status: {status}")

# Traditional if-else (for comparison)
age = 15
if age >= 18:
    status = "adult"
else:
    status = "minor"
print(f"Age: {age}, Status: {status}")

# Ternary with numbers
number = 10
result = "positive" if number > 0 else "non-positive"
print(f"{number} is {result}")

# Ternary with calculations
score = 85
grade = "Pass" if score >= 60 else "Fail"
print(f"Score: {score}, Grade: {grade}")

# Ternary in print statement
temperature = 25
print(f"It's {'hot' if temperature > 30 else 'comfortable'}")

# Nested ternary (use with caution)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Score: {score}, Grade: {grade}")

# Ternary with function calls
def get_discount(is_member):
    return 0.10 if is_member else 0

discount = get_discount(True)
print(f"Discount: {discount * 100}%")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Absolute value
number = -5
absolute = number if number >= 0 else -number
print(f"Absolute value of {number}: {absolute}")

# Example 2: Max of two numbers
a, b = 10, 20
maximum = a if a > b else b
print(f"Maximum of {a} and {b}: {maximum}")

# Example 3: Even or odd
number = 7
parity = "even" if number % 2 == 0 else "odd"
print(f"{number} is {parity}")

# Example 4: Discount calculator
price = 100
is_member = True
final_price = price * 0.9 if is_member else price
print(f"Price: ${price}, Member: {is_member}, Final: ${final_price}")

# Example 5: Empty list check
items = []
message = f"You have {len(items)} items" if items else "List is empty"
print(message)

# Example 6: Temperature warning
temp = 38
warning = "High temperature!" if temp > 37.5 else "Normal"
print(f"Temperature: {temp}°C - {warning}")

# Example 7: Sign of number
num = -10
sign = "positive" if num > 0 else "negative" if num < 0 else "zero"
print(f"{num} is {sign}")

# Example 8: Plural form
count = 1
word = "item" if count == 1 else "items"
print(f"You have {count} {word}")

count = 5
word = "item" if count == 1 else "items"
print(f"You have {count} {word}")

# Example 9: Login status
is_logged_in = False
welcome_message = "Welcome back!" if is_logged_in else "Please log in"
print(welcome_message)

# Example 10: Access level
user_role = "admin"
access = "Full access" if user_role == "admin" else "Limited access"
print(f"Role: {user_role}, Access: {access}")

# Example 11: Grade symbol
score = 92
symbol = "+" if score >= 97 else "-" if score < 90 else ""
print(f"Score: {score}, Grade: A{symbol}")

# Example 12: List operations
numbers = [1, 2, 3, 4, 5]
first = numbers[0] if numbers else None
print(f"First element: {first}")

empty_list = []
first = empty_list[0] if empty_list else None
print(f"First element of empty list: {first}")

# Example 13: String formatting
name = ""
display_name = name if name else "Anonymous"
print(f"Display name: {display_name}")

name = "John"
display_name = name if name else "Anonymous"
print(f"Display name: {display_name}")

# Example 14: Comparison result
x, y = 10, 20
relation = f"{x} > {y}" if x > y else f"{x} < {y}" if x < y else f"{x} = {y}"
print(relation)

# Example 15: Age category
age = 25
category = "child" if age < 13 else "teen" if age < 18 else "adult"
print(f"Age {age}: {category}")
