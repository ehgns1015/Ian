"""
List Comprehensions

List comprehensions provide a concise way to create lists.
They are more readable and often faster than traditional loops.

Syntax: [expression for item in iterable if condition]

Source: 00_review_and_more.docx - Section 7: Lists - List Comprehensions
"""

# ===== BASIC LIST COMPREHENSION =====
print("=== BASIC LIST COMPREHENSION ===\n")

# Creating list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Traditional way (for comparison)
squares_traditional = []
for x in range(1, 6):
    squares_traditional.append(x**2)
print(f"Traditional method: {squares_traditional}")

# Creating list from another list
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(f"\nOriginal: {numbers}")
print(f"Doubled: {doubled}")

# ===== WITH CONDITION =====
print("\n=== WITH CONDITION ===\n")

# Even numbers only
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers (1-10): {even_numbers}")

# Odd numbers only
odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print(f"Odd numbers (1-10): {odd_numbers}")

# Numbers divisible by 3
divisible_by_3 = [x for x in range(1, 21) if x % 3 == 0]
print(f"Divisible by 3 (1-20): {divisible_by_3}")

# ===== STRING OPERATIONS =====
print("\n=== STRING OPERATIONS ===\n")

# Uppercase all strings
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Original: {words}")
print(f"Uppercase: {uppercase}")

# Get lengths
lengths = [len(word) for word in words]
print(f"Lengths: {lengths}")

# Filter by length
names = ["Alice", "Bob", "Charlie", "Dan"]
long_names = [name for name in names if len(name) > 3]
print(f"\nAll names: {names}")
print(f"Names longer than 3 characters: {long_names}")

# ===== NESTED LIST COMPREHENSION =====
print("\n=== NESTED LIST COMPREHENSION ===\n")

# Create coordinates
coordinates = [(x, y) for x in range(3) for y in range(2)]
print(f"Coordinates: {coordinates}")

# Multiplication table
table = [[x * y for y in range(1, 6)] for x in range(1, 6)]
print("\nMultiplication table:")
for row in table:
    print(row)

# ===== WITH IF-ELSE =====
print("\n=== WITH IF-ELSE ===\n")

# Label numbers as even or odd
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Numbers: {numbers}")
print(f"Labels: {labels}")

# Replace negative with zero
values = [5, -2, 8, -7, 3]
positive_only = [x if x > 0 else 0 for x in values]
print(f"\nOriginal: {values}")
print(f"Negatives as zero: {positive_only}")

# ===== MATHEMATICAL OPERATIONS =====
print("\n=== MATHEMATICAL OPERATIONS ===\n")

# Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Square root approximation
numbers = [1, 4, 9, 16, 25]
roots = [x ** 0.5 for x in numbers]
print(f"\nNumbers: {numbers}")
print(f"Square roots: {roots}")

# ===== FILTERING FROM EXISTING LIST =====
print("\n=== FILTERING ===\n")

# Filter positive numbers
mixed = [-5, 3, -1, 8, -9, 2, 0]
positive = [x for x in mixed if x > 0]
print(f"Mixed: {mixed}")
print(f"Positive only: {positive}")

# Filter vowels
text = "Hello World"
vowels = [char for char in text if char.lower() in 'aeiou']
print(f"\nText: '{text}'")
print(f"Vowels: {vowels}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Extract even squares
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares (1-10): {even_squares}")

# Example 2: Process prices with tax
prices = [10.00, 20.00, 15.50, 30.00]
tax_rate = 0.08
with_tax = [price * (1 + tax_rate) for price in prices]
print(f"\nPrices: {prices}")
print(f"With tax (8%): {[f'${p:.2f}' for p in with_tax]}")

# Example 3: Extract words starting with 'P'
words = ["Python", "Java", "PHP", "JavaScript", "Perl"]
p_words = [word for word in words if word.startswith('P')]
print(f"\nAll words: {words}")
print(f"Words starting with 'P': {p_words}")

# Example 4: Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in nested for num in sublist]
print(f"\nNested: {nested}")
print(f"Flattened: {flattened}")

# Example 5: Create initials
names = ["John Doe", "Jane Smith", "Bob Johnson"]
initials = [''.join([word[0] for word in name.split()]) for name in names]
print(f"\nNames: {names}")
print(f"Initials: {initials}")
