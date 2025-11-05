"""
String Methods

Python strings have many built-in methods for manipulation:
- Case conversion: upper(), lower(), title(), capitalize()
- Finding: find(), index(), count()
- Replacing: replace()
- Trimming: strip(), lstrip(), rstrip()
- Splitting/Joining: split(), join()

Source: 00_review_and_more.docx - Section 6: String Manipulation - String Methods
"""

# ===== CASE CONVERSION =====
print("=== CASE CONVERSION ===\n")

message = "Hello, World!"
print(f"Original: '{message}'")

# Convert to uppercase
upper_message = message.upper()
print(f"upper(): '{upper_message}'")

# Convert to lowercase
lower_message = message.lower()
print(f"lower(): '{lower_message}'")

# Title case (first letter of each word capitalized)
title_message = message.title()
print(f"title(): '{title_message}'")

# Capitalize first letter only
text = "hello world"
capitalized = text.capitalize()
print(f"\nOriginal: '{text}'")
print(f"capitalize(): '{capitalized}'")

# Swap case
mixed = "Hello World"
swapped = mixed.swapcase()
print(f"\nOriginal: '{mixed}'")
print(f"swapcase(): '{swapped}'")

# ===== FINDING SUBSTRINGS =====
print("\n=== FINDING SUBSTRINGS ===\n")

text = "Hello, World! Welcome to Python World!"
print(f"Text: '{text}'")

# Find substring (returns index or -1)
position = text.find("World")
print(f"find('World'): {position}")

position = text.find("Python")
print(f"find('Python'): {position}")

not_found = text.find("Java")
print(f"find('Java'): {not_found}")  # -1 if not found

# Count occurrences
count = text.count("World")
print(f"\ncount('World'): {count}")

count = text.count("o")
print(f"count('o'): {count}")

# ===== REPLACING =====
print("\n=== REPLACING ===\n")

message = "Hello, World!"
print(f"Original: '{message}'")

# Replace substring
new_message = message.replace("World", "Python")
print(f"replace('World', 'Python'): '{new_message}'")

# Replace multiple occurrences
text = "apple, apple, banana"
replaced = text.replace("apple", "orange")
print(f"\nOriginal: '{text}'")
print(f"replace('apple', 'orange'): '{replaced}'")

# Replace with count limit
text = "one one one one"
replaced = text.replace("one", "two", 2)  # Replace first 2 occurrences
print(f"\nOriginal: '{text}'")
print(f"replace('one', 'two', 2): '{replaced}'")

# ===== TRIMMING WHITESPACE =====
print("\n=== TRIMMING WHITESPACE ===\n")

text = "   Hello, World!   "
print(f"Original: '{text}'")

# Remove whitespace from both ends
stripped = text.strip()
print(f"strip(): '{stripped}'")

# Remove whitespace from left
left_stripped = text.lstrip()
print(f"lstrip(): '{left_stripped}'")

# Remove whitespace from right
right_stripped = text.rstrip()
print(f"rstrip(): '{right_stripped}'")

# Remove specific characters
text = "***Hello***"
cleaned = text.strip("*")
print(f"\nOriginal: '{text}'")
print(f"strip('*'): '{cleaned}'")

# ===== SPLITTING AND JOINING =====
print("\n=== SPLITTING AND JOINING ===\n")

# Split string into list
sentence = "Python is awesome"
words = sentence.split(" ")
print(f"Original: '{sentence}'")
print(f"split(' '): {words}")

# Split by comma
csv_data = "apple,banana,cherry"
items = csv_data.split(",")
print(f"\nOriginal: '{csv_data}'")
print(f"split(','): {items}")

# Split with no argument (splits on whitespace)
text = "Hello   World  Python"
words = text.split()
print(f"\nOriginal: '{text}'")
print(f"split(): {words}")

# Join list into string
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"\nList: {words}")
print(f"' '.join(): '{sentence}'")

# Join with different separator
items = ["apple", "banana", "cherry"]
result = ", ".join(items)
print(f"\nList: {items}")
print(f"', '.join(): '{result}'")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Clean user input
user_input = "  JohnDoe@email.com  "
cleaned = user_input.strip().lower()
print(f"User input: '{user_input}'")
print(f"Cleaned: '{cleaned}'")

# Example 2: Parse CSV line
csv_line = "John,Doe,30,New York"
fields = csv_line.split(",")
print(f"\nCSV: '{csv_line}'")
print(f"Parsed: {fields}")
print(f"First name: {fields[0]}")
print(f"Last name: {fields[1]}")

# Example 3: Create URL slug
title = "Hello World! Welcome to Python"
slug = title.lower().replace(" ", "-").replace("!", "")
print(f"\nTitle: '{title}'")
print(f"URL slug: '{slug}'")

# Example 4: Format phone number
phone = "5551234567"
formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print(f"\nPhone: '{phone}'")
print(f"Formatted: '{formatted}'")
