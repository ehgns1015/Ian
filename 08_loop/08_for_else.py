"""
For-Else Statement

Python's for loop can have an optional else clause.
The else block executes after the loop completes normally (without break).
If the loop is terminated by break, the else block is skipped.

Source: 01_for_loop.docx - Section 9: For Loop with else Clause
"""

# Basic for-else (loop completes normally)
print("=== LOOP COMPLETES NORMALLY ===\n")

for i in range(3):
    print(i)
else:
    print("Loop completed!")

# For-else with break (else skipped)
print("\n=== LOOP TERMINATED BY BREAK ===\n")

for i in range(3):
    print(i)
    if i == 1:
        break
else:
    print("This will not be printed")

print("After loop")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Check if number is prime
print("=== PRIME NUMBER CHECK ===")
number = 17

if number < 2:
    print(f"{number} is not prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not prime (divisible by {i})")
            break
    else:
        print(f"{number} is prime")

# Test with non-prime
print()
number = 15
if number < 2:
    print(f"{number} is not prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not prime (divisible by {i})")
            break
    else:
        print(f"{number} is prime")

# Example 2: Search in list
print("\n=== SEARCH IN LIST ===")
names = ['Alice', 'Bob', 'Charlie', 'David']
search_name = 'Eve'

for name in names:
    if name == search_name:
        print(f"Found: {search_name}")
        break
else:
    print(f"{search_name} not found in the list")

# Example 3: Validate all items
print("\n=== VALIDATE ALL ITEMS ===")
scores = [85, 90, 78, 92, 88]
minimum = 60

for score in scores:
    if score < minimum:
        print(f"Validation failed: {score} is below minimum {minimum}")
        break
else:
    print("All scores pass the minimum threshold")

# Test with failing data
print()
scores = [85, 90, 55, 92, 88]
for score in scores:
    if score < minimum:
        print(f"Validation failed: {score} is below minimum {minimum}")
        break
else:
    print("All scores pass the minimum threshold")

# Example 4: Check password attempts
print("\n=== PASSWORD ATTEMPTS ===")
attempts = ['pass123', 'secret', 'admin']
correct_password = 'admin123'
max_attempts = 3

for attempt in attempts:
    print(f"Attempt: {attempt}")
    if attempt == correct_password:
        print("Access granted!")
        break
else:
    print("Access denied: Maximum attempts reached")

# Example 5: Find matching item
print("\n=== FIND MATCHING ITEM ===")
inventory = [
    {'item': 'apple', 'quantity': 10},
    {'item': 'banana', 'quantity': 5},
    {'item': 'cherry', 'quantity': 15}
]

search_item = 'banana'
for product in inventory:
    if product['item'] == search_item:
        print(f"Found: {search_item}, Quantity: {product['quantity']}")
        break
else:
    print(f"{search_item} not in inventory")

# Example 6: Check for duplicates
print("\n=== CHECK FOR DUPLICATES ===")
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(f"Duplicate found: {numbers[i]}")
            break
    else:
        continue
    break
else:
    print("No duplicates found")

# Test with duplicates
print()
numbers = [1, 2, 3, 2, 5]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(f"Duplicate found: {numbers[i]}")
            break
    else:
        continue
    break
else:
    print("No duplicates found")

# Example 7: Process all or none
print("\n=== PROCESS ALL OR NONE ===")
data = [10, 20, 30, 40, 50]

print("Processing data:")
for value in data:
    if value < 0:
        print(f"Invalid value: {value}. Aborting.")
        break
    print(f"Processed: {value}")
else:
    print("All data processed successfully")

# Example 8: Search with fallback
print("\n=== SEARCH WITH FALLBACK ===")
users = [
    {'username': 'alice', 'role': 'admin'},
    {'username': 'bob', 'role': 'user'}
]

search_user = 'charlie'
for user in users:
    if user['username'] == search_user:
        print(f"User: {search_user}, Role: {user['role']}")
        break
else:
    print(f"User {search_user} not found. Creating default user.")
    users.append({'username': search_user, 'role': 'guest'})
    print(f"Created user: {search_user} with role: guest")

# Example 9: Validate input sequence
print("\n=== VALIDATE INPUT SEQUENCE ===")
inputs = ['5', '10', '15', '20']

print("Validating inputs:")
for inp in inputs:
    try:
        num = int(inp)
        if num <= 0:
            print(f"Invalid: {inp} must be positive")
            break
    except ValueError:
        print(f"Invalid: {inp} is not a number")
        break
else:
    print("All inputs are valid")

# Example 10: Countdown with completion
print("\n=== COUNTDOWN ===")
for i in range(5, 0, -1):
    print(f"{i}...")
    if i == 3:
        # Uncomment to test break
        # print("Aborted!")
        # break
        pass
else:
    print("Launch!")

# Example 11: Check all conditions
print("\n=== CHECK ALL CONDITIONS ===")
requirements = [True, True, True, True]

for index, req in enumerate(requirements):
    if not req:
        print(f"Requirement {index + 1} failed")
        break
else:
    print("All requirements met")
