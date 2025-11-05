"""
Print Function

The print() function displays output to the console.
It can handle multiple arguments and various data types.

Source: 00_review_and_more.docx - Section 5: Input and Output - Output
"""

# Basic printing
print("Hello, World!")

# Printing multiple items
name = "John"
age = 30
print("Name:", name, "Age:", age)

# Printing different data types
print("\n=== Different Data Types ===")
print("String:", "Hello")
print("Integer:", 42)
print("Float:", 3.14)
print("Boolean:", True)
print("List:", [1, 2, 3])
print("Dictionary:", {"key": "value"})

# Printing calculations
print("\n=== Printing Calculations ===")
print("10 + 5 =", 10 + 5)
print("10 * 3 =", 10 * 3)
print("20 / 4 =", 20 / 4)

# Printing with concatenation (only for strings)
print("\n=== String Concatenation ===")
first_name = "John"
last_name = "Doe"
print("Full name: " + first_name + " " + last_name)

# Can't concatenate string with number directly
# This would cause an error:
# print("Age: " + 30)  # TypeError

# Need to convert to string first:
print("Age: " + str(30))

# Printing with comma separator (automatic spacing)
print("\n=== Comma Separator ===")
print("Python", "is", "awesome")  # Adds space between items

# Printing variables
print("\n=== Printing Variables ===")
city = "New York"
temperature = 72
print("City:", city)
print("Temperature:", temperature, "°F")

# Printing empty line
print("\n=== Empty Lines ===")
print("Line 1")
print()  # Empty line
print("Line 3")

# Printing special characters
print("\n=== Special Characters ===")
print("Newline character: Line 1\nLine 2")
print("Tab character: Column1\tColumn2")
print("Backslash: C:\\Users\\Documents")
print("Quote: He said, \"Hello!\"")

# Printing multiplication of strings
print("\n=== String Repetition ===")
print("=" * 40)
print("*" * 20)
print("-" * 30)

# Practical example: Receipt
print("\n=== Receipt Example ===")
print("=" * 30)
print("       STORE RECEIPT")
print("=" * 30)
item1 = "Apple"
price1 = 1.50
item2 = "Banana"
price2 = 0.75
print("Item:", item1, "- Price: $", price1)
print("Item:", item2, "- Price: $", price2)
print("-" * 30)
total = price1 + price2
print("Total: $", total)
print("=" * 30)
