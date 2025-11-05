"""
Dictionary Methods

Dictionaries have various built-in methods:
- keys(): Get all keys
- values(): Get all values
- items(): Get all key-value pairs
- update(): Update dictionary with another dictionary
- clear(): Remove all items
- copy(): Create a shallow copy

Source: 00_review_and_more.docx - Section 9: Dictionaries - Dictionary Methods
"""

# ===== KEYS() METHOD =====
print("=== KEYS() ===\n")

person = {"name": "John", "age": 30, "city": "New York"}
print(f"Dictionary: {person}")

# Get all keys
keys = person.keys()
print(f"Keys: {keys}")
print(f"Type: {type(keys)}")

# Convert to list
keys_list = list(person.keys())
print(f"Keys as list: {keys_list}")

# Iterating over keys
print("Iterating over keys:")
for key in person.keys():
    print(f"  {key}")

# ===== VALUES() METHOD =====
print("\n=== VALUES() ===\n")

# Get all values
values = person.values()
print(f"Values: {values}")

# Convert to list
values_list = list(person.values())
print(f"Values as list: {values_list}")

# Iterating over values
print("Iterating over values:")
for value in person.values():
    print(f"  {value}")

# ===== ITEMS() METHOD =====
print("\n=== ITEMS() ===\n")

# Get all key-value pairs
items = person.items()
print(f"Items: {items}")

# Iterating over key-value pairs
print("Iterating over items:")
for key, value in person.items():
    print(f"  {key}: {value}")

# ===== UPDATE() METHOD =====
print("\n=== UPDATE() ===\n")

person = {"name": "John", "age": 30}
print(f"Original: {person}")

# Update with another dictionary
person.update({"age": 31, "city": "New York"})
print(f"After update: {person}")

# Update with keyword arguments
person.update(email="john@example.com", phone="555-1234")
print(f"After update with kwargs: {person}")

# ===== SETDEFAULT() METHOD =====
print("\n=== SETDEFAULT() ===\n")

person = {"name": "John", "age": 30}
print(f"Dictionary: {person}")

# Get existing key
name = person.setdefault("name", "Unknown")
print(f"setdefault('name', 'Unknown'): {name}")

# Add new key with default value
country = person.setdefault("country", "USA")
print(f"setdefault('country', 'USA'): {country}")
print(f"Dictionary after setdefault: {person}")

# ===== COPY() METHOD =====
print("\n=== COPY() ===\n")

original = {"name": "John", "age": 30}
print(f"Original: {original}")

# Create a copy
copied = original.copy()
print(f"Copied: {copied}")

# Modify copy
copied["age"] = 31
print(f"\nAfter modifying copy:")
print(f"Original: {original}")
print(f"Copied: {copied}")

# ===== CLEAR() METHOD =====
print("\n=== CLEAR() ===\n")

temp = {"a": 1, "b": 2, "c": 3}
print(f"Before clear: {temp}")

temp.clear()
print(f"After clear: {temp}")

# ===== FROMKEYS() METHOD =====
print("\n=== FROMKEYS() ===\n")

# Create dictionary from keys with same value
keys = ["name", "age", "city"]
person = dict.fromkeys(keys, "Unknown")
print(f"Created from keys: {person}")

# With specific default value
numbers = dict.fromkeys([1, 2, 3], 0)
print(f"Numbers: {numbers}")

# ===== GET() WITH DEFAULT =====
print("\n=== GET() WITH DEFAULT ===\n")

config = {"theme": "dark", "language": "English"}
print(f"Config: {config}")

# Get existing key
theme = config.get("theme", "light")
print(f"Theme: {theme}")

# Get non-existing key with default
font = config.get("font", "Arial")
print(f"Font: {font}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Counting items
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
fruit_count = {}

for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

print("Fruit count:")
for fruit, count in fruit_count.items():
    print(f"  {fruit}: {count}")

# Example 2: Merging configurations
default_config = {
    "theme": "light",
    "font_size": 12,
    "auto_save": True
}

user_config = {
    "theme": "dark",
    "font_size": 14
}

# Merge configurations (user overrides default)
final_config = default_config.copy()
final_config.update(user_config)

print(f"\nDefault config: {default_config}")
print(f"User config: {user_config}")
print(f"Final config: {final_config}")

# Example 3: Grade book
grades = {
    "Alice": [85, 90, 88],
    "Bob": [75, 80, 78],
    "Charlie": [95, 92, 94]
}

print("\nGrade Report:")
for student, scores in grades.items():
    average = sum(scores) / len(scores)
    print(f"  {student}: {scores} - Average: {average:.2f}")

# Example 4: Inventory management
inventory = {}

# Add items
inventory.setdefault("apples", 0)
inventory["apples"] += 10

inventory.setdefault("bananas", 0)
inventory["bananas"] += 5

print(f"\nInventory: {inventory}")

# Example 5: User preferences with defaults
user_prefs = {"notifications": True}
default_prefs = {
    "notifications": False,
    "theme": "light",
    "language": "English"
}

# Apply defaults for missing keys
for key, value in default_prefs.items():
    user_prefs.setdefault(key, value)

print(f"\nUser preferences: {user_prefs}")
