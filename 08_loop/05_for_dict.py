"""
For Loop with Dictionaries

Dictionaries can be iterated in several ways:
- keys only (default)
- values only
- key-value pairs

Source: 01_for_loop.docx - Section 4: Iterating Over Dictionaries
"""

# Iterating over keys (default)
print("=== ITERATING OVER KEYS (DEFAULT) ===\n")

person = {'name': 'John', 'age': 30, 'job': 'developer'}

for key in person:
    print(key)

# Explicit keys() method
print("\n=== KEYS() METHOD ===\n")

for key in person.keys():
    print(f"Key: {key}")

# Iterating over values
print("\n=== ITERATING OVER VALUES ===\n")

for value in person.values():
    print(value)

# Iterating over key-value pairs
print("\n=== ITERATING OVER ITEMS ===\n")

for key, value in person.items():
    print(f"{key}: {value}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Display formatted data
print("=== USER PROFILE ===")
user = {
    'username': 'john_doe',
    'email': 'john@example.com',
    'age': 28,
    'city': 'New York',
    'verified': True
}

for key, value in user.items():
    print(f"{key.capitalize()}: {value}")

# Example 2: Calculate average grade
print("\n=== STUDENT GRADES ===")
grades = {'Math': 85, 'English': 90, 'Science': 88, 'History': 92}

print("Grades:")
total = 0
for subject, grade in grades.items():
    print(f"  {subject}: {grade}")
    total += grade

average = total / len(grades)
print(f"Average: {average:.2f}")

# Example 3: Filter by value
print("\n=== INVENTORY CHECK ===")
inventory = {
    'apples': 50,
    'bananas': 5,
    'oranges': 30,
    'grapes': 2
}

print("Low stock items (< 10):")
for item, quantity in inventory.items():
    if quantity < 10:
        print(f"  {item}: {quantity}")

# Example 4: Count character frequency
print("\n=== CHARACTER FREQUENCY ===")
text = "hello world"
freq = {}

for char in text:
    if char != ' ':
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

print(f"Text: '{text}'")
for char, count in freq.items():
    print(f"  '{char}': {count}")

# Example 5: Convert units
print("\n=== TEMPERATURE CONVERSION ===")
cities_celsius = {
    'New York': 20,
    'Los Angeles': 25,
    'Chicago': 15,
    'Houston': 30
}

print("City Temperatures:")
for city, celsius in cities_celsius.items():
    fahrenheit = (celsius * 9/5) + 32
    print(f"  {city}: {celsius}°C / {fahrenheit}°F")

# Example 6: Find maximum value
print("\n=== FIND HIGHEST SCORE ===")
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92, 'David': 98}

max_score = 0
max_student = ""

for student, score in scores.items():
    if score > max_score:
        max_score = score
        max_student = student

print(f"Highest score: {max_student} with {max_score}")

# Example 7: Build new dictionary
print("\n=== APPLY DISCOUNT ===")
prices = {'laptop': 1000, 'mouse': 30, 'keyboard': 80}
discount = 0.10

discounted_prices = {}
for product, price in prices.items():
    discounted_prices[product] = price * (1 - discount)

print("Discounted Prices:")
for product, price in discounted_prices.items():
    print(f"  {product}: ${price:.2f}")

# Example 8: Nested dictionary
print("\n=== NESTED DICTIONARY ===")
students = {
    'student1': {'name': 'Alice', 'age': 20, 'grade': 'A'},
    'student2': {'name': 'Bob', 'age': 21, 'grade': 'B'},
    'student3': {'name': 'Charlie', 'age': 19, 'grade': 'A'}
}

print("Student Records:")
for student_id, info in students.items():
    print(f"\n{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")

# Example 9: Update values in loop
print("\n=== UPDATE INVENTORY ===")
stock = {'apples': 10, 'bananas': 5, 'oranges': 8}
restock = {'apples': 20, 'bananas': 15, 'pears': 12}

print("Before restock:", stock)
for item, quantity in restock.items():
    if item in stock:
        stock[item] += quantity
    else:
        stock[item] = quantity

print("After restock:", stock)

# Example 10: Multiple dictionaries
print("\n=== MERGE CONFIGURATIONS ===")
default_config = {'theme': 'light', 'font_size': 12, 'notifications': True}
user_config = {'theme': 'dark', 'font_size': 14}

print("Default settings:")
for key, value in default_config.items():
    print(f"  {key}: {value}")

print("\nUser settings:")
for key, value in user_config.items():
    print(f"  {key}: {value}")

# Merge (user overrides default)
final_config = default_config.copy()
for key, value in user_config.items():
    final_config[key] = value

print("\nFinal configuration:")
for key, value in final_config.items():
    print(f"  {key}: {value}")
