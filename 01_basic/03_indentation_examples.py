"""
Indentation in Python

Python uses indentation to define code blocks instead of curly braces.
Standard indentation is 4 spaces (not tabs).
Consistent indentation is required - incorrect indentation will cause errors.

Source: 00_review_and_more.docx - Section 2: Indentation
"""

# Example 1: Simple indentation with if statement
if True:
    print("This is indented with 4 spaces")
    print("This is also at the same indentation level")

# Example 2: Nested indentation
if True:
    print("First level of indentation")
    if True:
        print("Second level of indentation (8 spaces)")
        if True:
            print("Third level of indentation (12 spaces)")

# Example 3: Multiple code blocks
age = 25

if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

print("This line is not indented, so it's outside the if block")

# Example 4: Proper indentation matters
number = 10

if number > 5:
    print("Number is greater than 5")
    print("This is inside the if block")
print("This is outside the if block")
