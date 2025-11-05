"""
String Properties and Testing Methods

Python provides methods to check string properties:
- isalpha(): Check if all characters are alphabetic
- isdigit(): Check if all characters are digits
- isalnum(): Check if all characters are alphanumeric
- isspace(): Check if all characters are whitespace
- startswith(): Check if string starts with substring
- endswith(): Check if string ends with substring
- isupper(), islower(): Check case

Source: 00_review_and_more.docx - Section 6: String Manipulation - String Methods
"""

# ===== ALPHABETIC CHECK =====
print("=== ALPHABETIC CHECK ===\n")

text1 = "Hello"
text2 = "Hello123"
text3 = "Hello World"

print(f"'{text1}'.isalpha(): {text1.isalpha()}")  # True
print(f"'{text2}'.isalpha(): {text2.isalpha()}")  # False (contains digits)
print(f"'{text3}'.isalpha(): {text3.isalpha()}")  # False (contains space)

# ===== DIGIT CHECK =====
print("\n=== DIGIT CHECK ===\n")

num1 = "123"
num2 = "123.45"
num3 = "12a3"

print(f"'{num1}'.isdigit(): {num1.isdigit()}")  # True
print(f"'{num2}'.isdigit(): {num2.isdigit()}")  # False (contains period)
print(f"'{num3}'.isdigit(): {num3.isdigit()}")  # False (contains letter)

# ===== ALPHANUMERIC CHECK =====
print("\n=== ALPHANUMERIC CHECK ===\n")

text1 = "Hello123"
text2 = "Hello 123"
text3 = "Hello_123"

print(f"'{text1}'.isalnum(): {text1.isalnum()}")  # True
print(f"'{text2}'.isalnum(): {text2.isalnum()}")  # False (contains space)
print(f"'{text3}'.isalnum(): {text3.isalnum()}")  # False (contains underscore)

# ===== WHITESPACE CHECK =====
print("\n=== WHITESPACE CHECK ===\n")

text1 = "   "
text2 = "\t\n"
text3 = "Hello"
text4 = ""

print(f"'   '.isspace(): {text1.isspace()}")     # True
print(f"'\\t\\n'.isspace(): {text2.isspace()}")  # True
print(f"'Hello'.isspace(): {text3.isspace()}")   # False
print(f"''.isspace(): {text4.isspace()}")        # False (empty string)

# ===== STARTS WITH / ENDS WITH =====
print("\n=== STARTS WITH / ENDS WITH ===\n")

filename = "document.pdf"
url = "https://www.example.com"
greeting = "Hello, World!"

# startswith()
print(f"'{filename}'.startswith('doc'): {filename.startswith('doc')}")
print(f"'{url}'.startswith('https'): {url.startswith('https')}")
print(f"'{greeting}'.startswith('Hello'): {greeting.startswith('Hello')}")

# endswith()
print(f"\n'{filename}'.endswith('.pdf'): {filename.endswith('.pdf')}")
print(f"'{filename}'.endswith('.txt'): {filename.endswith('.txt')}")
print(f"'{greeting}'.endswith('!'): {greeting.endswith('!')}")

# ===== CASE CHECKS =====
print("\n=== CASE CHECKS ===\n")

upper_text = "HELLO"
lower_text = "hello"
mixed_text = "Hello"

# isupper()
print(f"'{upper_text}'.isupper(): {upper_text.isupper()}")  # True
print(f"'{mixed_text}'.isupper(): {mixed_text.isupper()}")  # False

# islower()
print(f"\n'{lower_text}'.islower(): {lower_text.islower()}")  # True
print(f"'{mixed_text}'.islower(): {mixed_text.islower()}")    # False

# istitle()
title_text = "Hello World"
not_title = "Hello world"
print(f"\n'{title_text}'.istitle(): {title_text.istitle()}")  # True
print(f"'{not_title}'.istitle(): {not_title.istitle()}")      # False

# ===== OTHER USEFUL CHECKS =====
print("\n=== OTHER CHECKS ===\n")

# isprintable() - Check if all characters are printable
text1 = "Hello World"
text2 = "Hello\nWorld"
print(f"'{text1}'.isprintable(): {text1.isprintable()}")  # True
print(f"'Hello\\nWorld'.isprintable(): {text2.isprintable()}")  # False

# isidentifier() - Check if valid Python identifier
var1 = "my_variable"
var2 = "2variable"
var3 = "my-variable"
print(f"\n'{var1}'.isidentifier(): {var1.isidentifier()}")  # True
print(f"'{var2}'.isidentifier(): {var2.isidentifier()}")    # False (starts with digit)
print(f"'{var3}'.isidentifier(): {var3.isidentifier()}")    # False (contains hyphen)

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Validate username (only letters and numbers)
username = "john123"
if username.isalnum():
    print(f"Username '{username}' is valid")
else:
    print(f"Username '{username}' is invalid")

# Example 2: Check file extension
filename = "photo.jpg"
if filename.endswith(('.jpg', '.png', '.gif')):
    print(f"'{filename}' is an image file")
else:
    print(f"'{filename}' is not an image file")

# Example 3: Validate numeric input
user_input = "123"
if user_input.isdigit():
    number = int(user_input)
    print(f"Valid number: {number}")
else:
    print(f"'{user_input}' is not a valid number")

# Example 4: Check if password is all lowercase
password = "mypassword"
if password.islower():
    print("Warning: Password should contain uppercase letters")
else:
    print("Password case is good")

# Example 5: Validate email domain
email = "user@example.com"
if email.endswith('@gmail.com'):
    print("Gmail account")
elif email.endswith('@yahoo.com'):
    print("Yahoo account")
else:
    print("Other email provider")

# Example 6: Check URL protocol
url = "https://www.example.com"
if url.startswith('https://'):
    print("Secure connection (HTTPS)")
elif url.startswith('http://'):
    print("Insecure connection (HTTP)")
else:
    print("Invalid URL format")
