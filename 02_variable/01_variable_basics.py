"""
Variables and Variable Naming Rules

Variables are containers for storing data values.
Python has no command for declaring variables - a variable is created
when you first assign a value to it.

Source: 00_review_and_more.docx - Section 3: Variables
"""

# Basic variable assignment
name = "John"
age = 30
height = 5.9
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# Multiple assignment
x, y, z = 1, 2, 3
print("\nMultiple assignment:")
print("x =", x, ", y =", y, ", z =", z)

# Same value to multiple variables
a = b = c = 100
print("\nSame value to multiple variables:")
print("a =", a, ", b =", b, ", c =", c)

# Variable reassignment
count = 10
print("\nOriginal count:", count)
count = 20
print("Updated count:", count)

# Variables can change type
value = 5       # integer
print("\nValue as integer:", value)
value = "Five"  # now it's a string
print("Value as string:", value)

"""
Variable Naming Rules:
1. Can contain letters, numbers, and underscores
2. Cannot start with a number
3. Cannot use reserved words (if, for, while, etc.)
4. Case-sensitive (age and Age are different)
5. Use descriptive names for readability
"""

# Good variable names
user_name = "Alice"
total_price = 99.99
is_active = True

# Case-sensitive demonstration
age = 25
Age = 30
AGE = 35

print("\nCase sensitivity:")
print("age:", age)
print("Age:", Age)
print("AGE:", AGE)
