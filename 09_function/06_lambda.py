"""
Lambda Functions

Lambda functions are small anonymous functions defined with the lambda keyword.
Syntax: lambda arguments: expression

They are useful for short, simple operations.

Source: 03_function.docx - Lambda Functions
"""

# Basic lambda function
square = lambda x: x ** 2

print("=== BASIC LAMBDA ===\n")
print(f"Square of 5: {square(5)}")
print(f"Square of 10: {square(10)}")

# Lambda with multiple parameters
add = lambda a, b: a + b
multiply = lambda a, b: a * b

print("\n=== MULTIPLE PARAMETERS ===\n")
print(f"5 + 3 = {add(5, 3)}")
print(f"5 * 3 = {multiply(5, 3)}")

# Comparison with regular function
print("\n=== REGULAR VS LAMBDA ===\n")

# Regular function
def double_regular(x):
    return x * 2

# Lambda function
double_lambda = lambda x: x * 2

print(f"Regular: {double_regular(5)}")
print(f"Lambda: {double_lambda(5)}")

# Lambda in map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

print("\n=== LAMBDA WITH MAP ===\n")
print(f"Numbers: {numbers}")
print(f"Squared: {squared}")

# Lambda in filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print("\n=== LAMBDA WITH FILTER ===\n")
print(f"Numbers: {numbers}")
print(f"Even numbers: {evens}")

# Lambda in sorted()
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

sorted_students = sorted(students, key=lambda s: s['grade'], reverse=True)

print("\n=== LAMBDA WITH SORTED ===\n")
print("Sorted by grade (high to low):")
for student in sorted_students:
    print(f"  {student['name']}: {student['grade']}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Temperature conversion
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

print("Temperature Conversions:")
for temp in [0, 25, 100]:
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")

# Example 2: Calculate percentage
percentage = lambda part, total: (part / total) * 100

print(f"\nPercentage: {percentage(25, 100)}%")
print(f"Percentage: {percentage(75, 200)}%")

# Example 3: String operations
to_upper = lambda s: s.upper()
get_initials = lambda name: ''.join([word[0] for word in name.split()])

print("\nString Operations:")
print(f"Uppercase: {to_upper('hello')}")
print(f"Initials of 'John Doe': {get_initials('John Doe')}")

# Example 4: List of tuples sorting
points = [(3, 5), (1, 2), (5, 1), (2, 8)]
sorted_by_x = sorted(points, key=lambda p: p[0])
sorted_by_y = sorted(points, key=lambda p: p[1])

print("\nSorting Points:")
print(f"Original: {points}")
print(f"Sorted by X: {sorted_by_x}")
print(f"Sorted by Y: {sorted_by_y}")

# Example 5: Filter ages
ages = [12, 25, 17, 30, 15, 22, 19]
adults = list(filter(lambda age: age >= 18, ages))

print(f"\nAges: {ages}")
print(f"Adults (>=18): {adults}")

# Example 6: Transform prices
prices = [10.00, 20.00, 15.50, 30.00]
with_tax = list(map(lambda p: p * 1.08, prices))

print("\nPrices with 8% tax:")
for original, taxed in zip(prices, with_tax):
    print(f"  ${original:.2f} -> ${taxed:.2f}")

# Example 7: Conditional lambda
max_of_two = lambda a, b: a if a > b else b

print(f"\nMax of 10 and 20: {max_of_two(10, 20)}")
print(f"Max of 50 and 30: {max_of_two(50, 30)}")

# Example 8: Lambda with reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

print(f"\nProduct of {numbers}: {product}")

# When to use lambda vs regular function
print("\n=== WHEN TO USE LAMBDA ===\n")
print("Use lambda for:")
print("- Short, simple operations")
print("- One-time use functions")
print("- As arguments to higher-order functions (map, filter, sorted)")
print("\nUse regular functions for:")
print("- Complex logic")
print("- Multiple statements")
print("- Reusable code")
print("- Better readability")
