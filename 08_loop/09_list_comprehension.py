"""
List Comprehension in Loops Context

List comprehensions provide a concise alternative to for loops
for creating lists. They are more readable and often faster.

Note: This topic is also covered in 06_data_structure/03_list_comprehension.py
Here we focus on the relationship with traditional for loops.

Source: 01_for_loop.docx - Section 6: List Comprehensions
"""

# Traditional for loop vs list comprehension
print("=== TRADITIONAL VS COMPREHENSION ===\n")

# Traditional way
squares_traditional = []
for x in range(1, 6):
    squares_traditional.append(x**2)
print(f"Traditional: {squares_traditional}")

# List comprehension
squares_comp = [x**2 for x in range(1, 6)]
print(f"Comprehension: {squares_comp}")

# With condition - traditional
print("\n=== WITH CONDITION ===\n")

# Traditional
evens_traditional = []
for x in range(1, 11):
    if x % 2 == 0:
        evens_traditional.append(x)
print(f"Traditional: {evens_traditional}")

# Comprehension
evens_comp = [x for x in range(1, 11) if x % 2 == 0]
print(f"Comprehension: {evens_comp}")

# Transform list - traditional vs comprehension
print("\n=== TRANSFORM LIST ===\n")

words = ["hello", "world", "python"]

# Traditional
uppercase_trad = []
for word in words:
    uppercase_trad.append(word.upper())
print(f"Traditional: {uppercase_trad}")

# Comprehension
uppercase_comp = [word.upper() for word in words]
print(f"Comprehension: {uppercase_comp}")

# Nested loops - traditional vs comprehension
print("\n=== NESTED LOOPS ===\n")

# Traditional
coordinates_trad = []
for x in range(3):
    for y in range(2):
        coordinates_trad.append((x, y))
print(f"Traditional: {coordinates_trad}")

# Comprehension
coordinates_comp = [(x, y) for x in range(3) for y in range(2)]
print(f"Comprehension: {coordinates_comp}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Filter and transform
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get squares of even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Example 2: String manipulation
names = ["alice", "bob", "charlie"]
capitalized = [name.capitalize() for name in names]
print(f"Capitalized: {capitalized}")

# Example 3: Extract from list of dicts
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]

names = [student['name'] for student in students]
high_scores = [s['name'] for s in students if s['score'] >= 85]

print(f"All names: {names}")
print(f"High scores (>=85): {high_scores}")

# Example 4: Mathematical operations
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Example 5: Conditional expression in comprehension
numbers = [-5, 3, -1, 8, -9, 2, 0]
positive_only = [x if x > 0 else 0 for x in numbers]
print(f"Original: {numbers}")
print(f"Positive only: {positive_only}")

# Example 6: Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in nested for num in sublist]
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")

# Example 7: Filter strings by length
words = ["a", "ab", "abc", "abcd", "abcde"]
long_words = [word for word in words if len(word) > 2]
print(f"Words: {words}")
print(f"Long words (>2): {long_words}")

# Example 8: Multiple conditions
numbers = range(1, 21)
special = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(f"Divisible by both 2 and 3 (1-20): {special}")

# Example 9: Extract file extensions
files = ["doc1.txt", "image.png", "data.csv", "script.py"]
extensions = [file.split('.')[-1] for file in files]
print(f"Files: {files}")
print(f"Extensions: {extensions}")

# Example 10: Create dictionary using comprehension
print("\n=== DICTIONARY COMPREHENSION ===")
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# Example 11: Set comprehension
print("\n=== SET COMPREHENSION ===")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x**2 for x in numbers}
print(f"Unique squares: {unique_squares}")

# Example 12: Complex transformation
print("\n=== COMPLEX TRANSFORMATION ===")
data = [
    "Alice:25:New York",
    "Bob:30:Los Angeles",
    "Charlie:28:Chicago"
]

# Parse into list of dictionaries
parsed = [
    {'name': parts[0], 'age': int(parts[1]), 'city': parts[2]}
    for item in data
    for parts in [item.split(':')]
]

print("Parsed data:")
for person in parsed:
    print(f"  {person}")

# Performance comparison note
print("\n=== PERFORMANCE NOTE ===")
print("List comprehensions are generally faster than equivalent for loops")
print("because they are optimized at the C level in Python's interpreter.")
