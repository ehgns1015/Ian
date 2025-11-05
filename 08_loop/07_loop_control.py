"""
Loop Control Statements

Python provides three statements to control loop execution:
- break: Exit the loop immediately
- continue: Skip current iteration and jump to next
- pass: Do nothing (placeholder)

Source: 01_for_loop.docx - Section 8: Loop Control Statements
"""

# BREAK - Exit loop immediately
print("=== BREAK STATEMENT ===\n")

for i in range(10):
    if i == 5:
        break
    print(i)
print("Loop ended with break")

# Break with search
print("\n=== BREAK WITH SEARCH ===")
numbers = [1, 3, 5, 7, 9, 2, 4, 6]
target = 7

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}...")

# CONTINUE - Skip current iteration
print("\n=== CONTINUE STATEMENT ===\n")

for i in range(5):
    if i == 2:
        continue
    print(i)
print("Loop completed")

# Continue with filter
print("\n=== CONTINUE WITH FILTER ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Odd numbers only:")
for num in numbers:
    if num % 2 == 0:
        continue
    print(num, end=" ")
print()

# PASS - Do nothing (placeholder)
print("\n=== PASS STATEMENT ===\n")

for i in range(3):
    if i == 1:
        pass  # TODO: Add logic later
    print(i)

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Find first match
print("=== FIND FIRST MATCH ===")
names = ['Alice', 'Bob', 'Charlie', 'David']
search = 'Charlie'

for name in names:
    if name == search:
        print(f"Found: {name}")
        break
else:
    print(f"{search} not found")

# Example 2: Skip invalid data
print("\n=== SKIP INVALID DATA ===")
ages = [25, -5, 30, 0, 17, -3, 22]

print("Valid ages (positive):")
for age in ages:
    if age <= 0:
        continue
    print(age, end=" ")
print()

# Example 3: Stop on condition
print("\n=== STOP ON THRESHOLD ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
threshold = 20
total = 0

for num in numbers:
    total += num
    print(f"Adding {num}, total = {total}")
    if total >= threshold:
        print(f"Reached threshold of {threshold}")
        break

# Example 4: Process valid items only
print("\n=== PROCESS VALID ITEMS ===")
items = ['apple', '', 'banana', None, 'cherry', '']

print("Non-empty items:")
for item in items:
    if not item:
        continue
    print(f"  - {item}")

# Example 5: Nested loop with break
print("\n=== NESTED BREAK ===")
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

found_zero = False
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        if val == 0:
            print(f"Found 0 at position [{i}][{j}]")
            found_zero = True
            break
    if found_zero:
        break

# Example 6: Password validation with break
print("\n=== PASSWORD VALIDATION ===")
attempts = ['pass123', 'secret', 'admin123', 'correct_pass']
correct_password = 'admin123'

for attempt in attempts:
    print(f"Trying: {attempt}")
    if attempt == correct_password:
        print("Access granted!")
        break
else:
    print("All attempts failed")

# Example 7: Skip multiples of 3
print("\n=== SKIP MULTIPLES OF 3 ===")
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# Example 8: Break on error
print("\n=== BREAK ON ERROR ===")
numbers = [10, 20, 0, 30, 40]

print("Performing division:")
for num in numbers:
    if num == 0:
        print("Error: Cannot divide by zero!")
        break
    result = 100 / num
    print(f"100 / {num} = {result:.2f}")

# Example 9: Continue with try-except
print("\n=== CONTINUE WITH ERRORS ===")
values = ['10', '20', 'abc', '30', 'xyz']

total = 0
for val in values:
    try:
        total += int(val)
    except ValueError:
        print(f"Skipping invalid value: {val}")
        continue

print(f"Total: {total}")

# Example 10: Stop and continue combined
print("\n=== COMBINED CONTROL ===")
print("Numbers 1-20, skip multiples of 3, stop at first multiple of 15:")
for i in range(1, 21):
    if i % 3 == 0:
        if i % 15 == 0:
            print(f"\nStopping at {i}")
            break
        continue
    print(i, end=" ")
print()

# Example 11: Pass as placeholder
print("\n=== PASS AS PLACEHOLDER ===")
data = [1, 2, 3, 4, 5]

for item in data:
    if item < 3:
        pass  # TODO: Handle small numbers
    elif item == 3:
        pass  # TODO: Handle middle value
    else:
        print(f"Processing {item}")

# Example 12: Interactive search with break
print("\n=== SEARCH IN LIST ===")
products = ['laptop', 'mouse', 'keyboard', 'monitor', 'headphones']
search_term = 'keyboard'

found = False
for index, product in enumerate(products):
    if product == search_term:
        print(f"Found '{search_term}' at index {index}")
        found = True
        break

if not found:
    print(f"'{search_term}' not found")
