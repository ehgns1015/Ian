"""
String Operations

Strings support various operations:
- Concatenation (joining strings)
- Repetition (repeating strings)
- Indexing (accessing individual characters)
- Slicing (extracting substrings)

Source: 00_review_and_more.docx - Section 6: String Manipulation - String Operations
"""

# ===== CONCATENATION =====
print("=== STRING CONCATENATION ===\n")

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# Concatenating multiple strings
greeting = "Hello" + ", " + "World" + "!"
print("Greeting:", greeting)

# ===== REPETITION =====
print("\n=== STRING REPETITION ===\n")

line = "-" * 20
print(line)

stars = "*" * 10
print(stars)

# Creating patterns
print("=" * 40)
print("Python" * 3)
print("Ha" * 5)

# ===== INDEXING =====
print("\n=== STRING INDEXING ===\n")

message = "Hello"
print(f"String: '{message}'")

# Positive indexing (from start)
first_char = message[0]
print(f"First character (index 0): '{first_char}'")

second_char = message[1]
print(f"Second character (index 1): '{second_char}'")

# Negative indexing (from end)
last_char = message[-1]
print(f"Last character (index -1): '{last_char}'")

second_last = message[-2]
print(f"Second last (index -2): '{second_last}'")

# Index positions visualization
text = "Python"
print(f"\nString: '{text}'")
print("Positive indices: 0=P, 1=y, 2=t, 3=h, 4=o, 5=n")
print("Negative indices: -6=P, -5=y, -4=t, -3=h, -2=o, -1=n")

# ===== SLICING =====
print("\n=== STRING SLICING ===\n")

message = "Hello, World!"
print(f"Original string: '{message}'")

# Basic slicing [start:end]
substring = message[0:5]  # Characters from index 0 to 4
print(f"message[0:5]: '{substring}'")

# From beginning to index
substring = message[:5]  # Same as [0:5]
print(f"message[:5]: '{substring}'")

# From index to end
substring = message[7:]  # From index 7 to the end
print(f"message[7:]: '{substring}'")

# Last N characters
substring = message[-6:]  # Last 6 characters
print(f"message[-6:]: '{substring}'")

# Slicing with step
text = "Hello, World!"
print(f"\nString: '{text}'")

# Every 2nd character
print(f"Every 2nd char: '{text[::2]}'")

# Every 3rd character
print(f"Every 3rd char: '{text[::3]}'")

# Reverse string
print(f"Reversed: '{text[::-1]}'")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Extract domain from email
email = "user@example.com"
at_index = email.index("@")
domain = email[at_index + 1:]
print(f"Email: {email}")
print(f"Domain: {domain}")

# Example 2: Get file extension
filename = "document.pdf"
dot_index = filename.rindex(".")
extension = filename[dot_index + 1:]
print(f"\nFilename: {filename}")
print(f"Extension: {extension}")

# Example 3: Extract area code from phone
phone = "(555) 123-4567"
area_code = phone[1:4]
print(f"\nPhone: {phone}")
print(f"Area code: {area_code}")

# Example 4: Create initials
first = "John"
middle = "Michael"
last = "Doe"
initials = first[0] + "." + middle[0] + "." + last[0] + "."
print(f"\nFull name: {first} {middle} {last}")
print(f"Initials: {initials}")

# Example 5: Censoring middle part
credit_card = "1234567890123456"
visible = credit_card[:4] + "********" + credit_card[-4:]
print(f"\nCredit card: {credit_card}")
print(f"Censored: {visible}")
