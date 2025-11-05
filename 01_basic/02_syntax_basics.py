"""
Python Syntax Basics

Python uses indentation (whitespace) to define code blocks.
Comments are used to explain code and are ignored by the interpreter.

Source: 00_review_and_more.docx - Section 2: Python Syntax Basics
"""

# Single-line comment
# This is a comment explaining the code below

print("Python uses indentation for code blocks")

"""
This is a multi-line comment
or docstring that spans multiple lines.
You can use triple quotes for this purpose.
"""

# Python is case-sensitive
name = "John"
Name = "Jane"  # This is a different variable

print(name)  # Output: John
print(Name)  # Output: Jane

# Line continuation using backslash
total = 1 + 2 + 3 + \
        4 + 5 + 6

print("Total using backslash:", total)

# Line continuation using parentheses (preferred)
total_preferred = (1 + 2 + 3 +
                   4 + 5 + 6)

print("Total using parentheses:", total_preferred)
