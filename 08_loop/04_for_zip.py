"""
For Loop with zip()

zip() combines multiple iterables (lists, tuples, etc.) element by element.
It creates pairs/tuples from the elements at the same positions.
Stops when the shortest iterable is exhausted.

Source: 01_for_loop.docx - Section 5: The zip() Function
"""

# Basic zip with two lists
print("=== BASIC ZIP ===\n")

names = ['John', 'Jane', 'Michael']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Zip with three lists
print("\n=== ZIP THREE LISTS ===\n")

names = ['John', 'Jane', 'Michael']
ages = [25, 30, 35]
jobs = ['developer', 'designer', 'manager']

for name, age, job in zip(names, ages, jobs):
    print(f"{name} is {age} years old and works as a {job}.")

# Zip with different length lists
print("\n=== DIFFERENT LENGTHS ===\n")

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

# Stops at shortest list (length 3)
for num, letter in zip(list1, list2):
    print(f"{num} - {letter}")

# Zip with tuples
print("\n=== ZIP TUPLES ===\n")

first_names = ('Alice', 'Bob', 'Charlie')
last_names = ('Smith', 'Jones', 'Brown')

for first, last in zip(first_names, last_names):
    print(f"Full name: {first} {last}")

# Zip with range
print("\n=== ZIP WITH RANGE ===\n")

items = ['apple', 'banana', 'cherry']
for index, item in zip(range(1, 4), items):
    print(f"Item {index}: {item}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Combine lists into dictionary
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

person_dict = {}
for key, value in zip(keys, values):
    person_dict[key] = value

print(f"Dictionary: {person_dict}")

# Alternative: dict(zip(keys, values))
person_dict2 = dict(zip(keys, values))
print(f"Using dict(zip()): {person_dict2}")

# Example 2: Parallel iteration
print("\n=== CALCULATE TOTALS ===")
products = ['Laptop', 'Mouse', 'Keyboard']
prices = [999.99, 29.99, 79.99]
quantities = [1, 2, 1]

total_cost = 0
for product, price, qty in zip(products, prices, quantities):
    subtotal = price * qty
    total_cost += subtotal
    print(f"{product}: ${price} x {qty} = ${subtotal:.2f}")

print(f"Total: ${total_cost:.2f}")

# Example 3: Compare two lists
print("\n=== COMPARE LISTS ===")
expected = [5, 10, 15, 20]
actual = [5, 11, 15, 19]

for exp, act in zip(expected, actual):
    match = "✓" if exp == act else "✗"
    print(f"Expected: {exp}, Actual: {act} {match}")

# Example 4: Team roster
print("\n=== TEAM ROSTER ===")
players = ['Alice', 'Bob', 'Charlie', 'David']
positions = ['Forward', 'Guard', 'Center', 'Forward']
jerseys = [10, 23, 33, 7]

print("Team Roster:")
for player, position, jersey in zip(players, positions, jerseys):
    print(f"#{jersey} {player} - {position}")

# Example 5: Temperature conversion
print("\n=== TEMPERATURE TABLE ===")
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']
celsius = [20, 25, 15, 30]

print("City Temperature Chart:")
for city, temp_c in zip(cities, celsius):
    temp_f = (temp_c * 9/5) + 32
    print(f"{city}: {temp_c}°C / {temp_f}°F")

# Example 6: Create tuples from lists
print("\n=== CREATE TUPLES ===")
ids = [101, 102, 103]
usernames = ['alice', 'bob', 'charlie']
emails = ['alice@email.com', 'bob@email.com', 'charlie@email.com']

users = []
for user_id, username, email in zip(ids, usernames, emails):
    user_tuple = (user_id, username, email)
    users.append(user_tuple)

print("Users:")
for user in users:
    print(user)

# Example 7: Merge parallel data
print("\n=== STUDENT GRADES ===")
students = ['Alice', 'Bob', 'Charlie']
math_scores = [85, 90, 78]
english_scores = [88, 85, 92]

for student, math, english in zip(students, math_scores, english_scores):
    average = (math + english) / 2
    print(f"{student}: Math={math}, English={english}, Average={average:.1f}")

# Example 8: Unzip (reverse operation)
print("\n=== UNZIPPING ===")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)  # Unzip

print(f"Original pairs: {pairs}")
print(f"Numbers: {numbers}")
print(f"Letters: {letters}")

# Example 9: Parallel modification
print("\n=== PARALLEL MODIFICATION ===")
quantities = [10, 20, 15, 30]
adjustments = [2, -5, 3, -10]

print("Inventory Adjustments:")
for qty, adj in zip(quantities, adjustments):
    new_qty = qty + adj
    print(f"{qty} + ({adj}) = {new_qty}")

# Example 10: Match questions and answers
print("\n=== QUIZ ===")
questions = ['What is 2+2?', 'What is the capital of France?', 'What is H2O?']
answers = ['4', 'Paris', 'Water']
user_answers = ['4', 'Paris', 'Ice']

correct = 0
for q, ans, user_ans in zip(questions, answers, user_answers):
    is_correct = ans.lower() == user_ans.lower()
    if is_correct:
        correct += 1
    status = "Correct" if is_correct else f"Wrong (answer: {ans})"
    print(f"\nQ: {q}")
    print(f"Your answer: {user_ans} - {status}")

print(f"\nScore: {correct}/{len(questions)}")
