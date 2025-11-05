"""
Logical Operators

Logical operators are used to combine conditional statements.
They return a boolean value (True or False).

Operators: and, or, not

Source: 00_review_and_more.docx - Section 4: Basic Operators - Logical
"""

x = True
y = False

print(f"x = {x}, y = {y}\n")

# Logical AND
# Returns True only if both operands are True
result = x and y
print(f"x and y: {result}")  # False

result = True and True
print(f"True and True: {result}")  # True

result = False and True
print(f"False and True: {result}")  # False

# Logical OR
# Returns True if at least one operand is True
print("\n=== OR Operator ===")
result = x or y
print(f"x or y: {result}")  # True

result = False or False
print(f"False or False: {result}")  # False

result = False or True
print(f"False or True: {result}")  # True

# Logical NOT
# Reverses the boolean value
print("\n=== NOT Operator ===")
result = not x
print(f"not x: {result}")  # False

result = not y
print(f"not y: {result}")  # True

result = not False
print(f"not False: {result}")  # True

# Combining logical operators
print("\n=== Combining Operators ===")
a = True
b = False
c = True

result = a and b or c
print(f"a and b or c: {result}")  # True

result = a and (b or c)
print(f"a and (b or c): {result}")  # True

result = not (a and b)
print(f"not (a and b): {result}")  # True

# Practical examples with comparisons
print("\n=== Practical Examples ===")

age = 25
has_license = True

# Check if someone can drive
can_drive = age >= 18 and has_license
print(f"Age: {age}, Has license: {has_license}")
print(f"Can drive: {can_drive}")

# Check eligibility with multiple conditions
income = 50000
credit_score = 700
has_job = True

eligible_for_loan = (income > 30000 and credit_score > 650) and has_job
print(f"\nIncome: {income}, Credit score: {credit_score}, Has job: {has_job}")
print(f"Eligible for loan: {eligible_for_loan}")

# Using OR for validation
username = ""
email = "user@example.com"

has_credentials = username or email  # True if at least one is provided
print(f"\nUsername: '{username}', Email: '{email}'")
print(f"Has credentials: {bool(has_credentials)}")

# Short-circuit evaluation
print("\n=== Short-circuit Evaluation ===")
# AND: If first is False, second is not evaluated
result = False and print("This won't print")
print("False and ... results in:", result)

# OR: If first is True, second is not evaluated
result = True or print("This won't print either")
print("True or ... results in:", result)

# Truth table demonstration
print("\n=== Truth Table ===")
print("AND Truth Table:")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")

print("\nOR Truth Table:")
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")
