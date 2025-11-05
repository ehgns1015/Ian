"""
If-Else Statement

The if-else statement provides an alternative path when condition is False.
Either the if block or the else block will execute, but never both.

Source: 00_review_and_more.docx - Section 11: Conditional Statements - if-else Statement
"""

# Basic if-else
age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If-else with calculations
number = -5

if number >= 0:
    print(f"{number} is non-negative")
else:
    print(f"{number} is negative")

# If-else with string comparison
password = "wrongpass"
correct_password = "secret123"

if password == correct_password:
    print("Access granted")
else:
    print("Access denied")

# If-else with boolean variables
is_logged_in = False

if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in")

# If-else with multiple conditions (and)
age = 25
income = 50000

if age > 18 and income > 30000:
    print("Loan approved")
else:
    print("Loan denied")

# If-else with multiple conditions (or)
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Even or odd
number = 7

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Example 2: Pass or fail
score = 55
passing_score = 60

if score >= passing_score:
    print("Passed!")
    grade = "Pass"
else:
    print("Failed!")
    grade = "Fail"

print(f"Score: {score}, Grade: {grade}")

# Example 3: Discount calculator
purchase = 150
discount_threshold = 100

if purchase >= discount_threshold:
    discount = purchase * 0.1
    final_price = purchase - discount
    print(f"10% discount applied: ${discount:.2f}")
else:
    final_price = purchase
    print("No discount")

print(f"Final price: ${final_price:.2f}")

# Example 4: Temperature check
temperature = 32

if temperature > 30:
    print("It's hot! Stay hydrated.")
else:
    print("Temperature is comfortable.")

# Example 5: List empty check
shopping_list = []

if len(shopping_list) > 0:
    print(f"You have {len(shopping_list)} items")
else:
    print("Your shopping list is empty")

# Example 6: User authentication
username = "admin"
password = "pass123"

if username == "admin" and password == "pass123":
    print("Login successful")
else:
    print("Invalid credentials")

# Example 7: Number comparison
a = 10
b = 20

if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is less than or equal to {b}")
