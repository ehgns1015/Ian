"""
String Data Type

Strings are sequences of characters enclosed in quotes.
You can use single quotes, double quotes, or triple quotes.

Source: 00_review_and_more.docx - Section 3: Basic Data Types - Text Type
"""

# String with double quotes
name = "Python"
print("String with double quotes:", name)
print("Type:", type(name))

# String with single quotes
language = 'Programming'
print("\nString with single quotes:", language)

# Strings are the same regardless of quote type
str1 = "Hello"
str2 = 'Hello'
print("\nAre they equal?", str1 == str2)  # True

# String with quotes inside
quote1 = "He said, 'Hello!'"
quote2 = 'She replied, "Hi there!"'
print("\nQuote inside string:", quote1)
print("Quote inside string:", quote2)

# Multiline string using triple quotes
multiline_string = """This is a
multiline string that
spans multiple lines"""

print("\nMultiline string:")
print(multiline_string)

# Alternative multiline with triple single quotes
another_multiline = '''This also works
with triple single quotes'''

print("\nAnother multiline:")
print(another_multiline)

# Empty string
empty = ""
print("\nEmpty string length:", len(empty))

# String with escape characters
escaped = "First line\nSecond line\tTabbed"
print("\nString with escape characters:")
print(escaped)

# Raw string (ignores escape characters)
raw_string = r"C:\new\folder\test"
print("\nRaw string:", raw_string)
