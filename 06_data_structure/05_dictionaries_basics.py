"""
Dictionaries - Basics

Dictionaries are unordered, mutable collections of key-value pairs.
Keys must be unique and immutable (strings, numbers, tuples).
Dictionaries are created using curly braces {} or dict().

Source: 00_review_and_more.docx - Section 9: Dictionaries
"""

# ===== CREATING DICTIONARIES =====
print("=== CREATING DICTIONARIES ===\n")

# Empty dictionary
empty_dict = {}
print(f"Empty dict: {empty_dict}")

# Dictionary with items
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}")

# Using dict() constructor
student = dict(name="Alice", grade=95, subject="Math")
print(f"Student: {student}")

# Dictionary with mixed types
mixed = {
    "string_key": "value",
    1: "numeric key",
    (1, 2): "tuple key",
    "number": 42,
    "list": [1, 2, 3]
}
print(f"Mixed: {mixed}")

# ===== ACCESSING VALUES =====
print("\n=== ACCESSING VALUES ===\n")

person = {"name": "John", "age": 30, "city": "New York"}
print(f"Person: {person}")

# Using square brackets
name = person["name"]
print(f"Name: {name}")

age = person["age"]
print(f"Age: {age}")

# Using get() method (safer, returns None if key doesn't exist)
city = person.get("city")
print(f"City: {city}")

# get() with default value
country = person.get("country", "Unknown")
print(f"Country: {country}")  # Returns "Unknown" since key doesn't exist

# This would cause an error:
# phone = person["phone"]  # KeyError: 'phone'

# ===== MODIFYING DICTIONARIES =====
print("\n=== MODIFYING DICTIONARIES ===\n")

person = {"name": "John", "age": 30}
print(f"Original: {person}")

# Adding new key-value pair
person["email"] = "john@example.com"
print(f"After adding email: {person}")

# Updating existing value
person["age"] = 31
print(f"After updating age: {person}")

# Adding multiple items
person["phone"] = "555-1234"
person["country"] = "USA"
print(f"After adding phone and country: {person}")

# ===== REMOVING ITEMS =====
print("\n=== REMOVING ITEMS ===\n")

person = {"name": "John", "age": 30, "city": "New York", "email": "john@example.com"}
print(f"Original: {person}")

# pop() - Remove and return value
email = person.pop("email")
print(f"Popped email: {email}")
print(f"After pop: {person}")

# pop() with default
phone = person.pop("phone", "Not found")
print(f"Popped phone: {phone}")

# popitem() - Remove and return last item (Python 3.7+)
last_item = person.popitem()
print(f"Popped last item: {last_item}")
print(f"After popitem: {person}")

# del - Delete specific key
del person["age"]
print(f"After del age: {person}")

# ===== CHECKING KEYS =====
print("\n=== CHECKING KEYS ===\n")

person = {"name": "John", "age": 30, "city": "New York"}

# Check if key exists
if "name" in person:
    print("Name key exists")

if "email" not in person:
    print("Email key does not exist")

# ===== DICTIONARY LENGTH =====
print("\n=== LENGTH ===\n")

print(f"Person: {person}")
print(f"Number of keys: {len(person)}")

# ===== NESTED DICTIONARIES =====
print("\n=== NESTED DICTIONARIES ===\n")

users = {
    "user1": {
        "name": "Alice",
        "age": 25
    },
    "user2": {
        "name": "Bob",
        "age": 30
    }
}

print(f"Users: {users}")
print(f"User1 name: {users['user1']['name']}")
print(f"User2 age: {users['user2']['age']}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Student record
student = {
    "id": 12345,
    "name": "Alice Johnson",
    "email": "alice@school.edu",
    "gpa": 3.8,
    "major": "Computer Science"
}

print("Student Record:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Example 2: Product inventory
product = {
    "id": "A001",
    "name": "Laptop",
    "price": 999.99,
    "in_stock": True,
    "quantity": 15
}

print(f"\nProduct: {product['name']}")
print(f"Price: ${product['price']}")
print(f"Available: {product['quantity']} units")

# Example 3: Configuration settings
config = {
    "theme": "dark",
    "language": "English",
    "notifications": True,
    "auto_save": True
}

print(f"\nConfiguration:")
print(f"  Theme: {config['theme']}")
print(f"  Language: {config['language']}")
print(f"  Notifications: {'Enabled' if config['notifications'] else 'Disabled'}")

# Example 4: Word frequency counter
text = "hello world hello python"
word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"\nWord frequency: {word_count}")

# Example 5: Phone book
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

name_to_find = "Alice"
if name_to_find in phonebook:
    print(f"\n{name_to_find}'s phone: {phonebook[name_to_find]}")
