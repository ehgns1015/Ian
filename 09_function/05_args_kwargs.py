"""
*args and **kwargs

*args: Allows a function to accept any number of positional arguments
**kwargs: Allows a function to accept any number of keyword arguments

Source: 03_function.docx - Advanced Parameters
"""

# *args - Variable number of positional arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("=== *ARGS - POSITIONAL ARGUMENTS ===\n")
print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40): {sum_all(10, 20, 30, 40)}")
print(f"sum_all(5): {sum_all(5)}")

# **kwargs - Variable number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n=== **KWARGS - KEYWORD ARGUMENTS ===\n")
print_info(name="Alice", age=25, city="New York")
print()
print_info(product="Laptop", price=999.99, in_stock=True)

# Combining regular parameters with *args
def multiply_by(multiplier, *numbers):
    results = []
    for num in numbers:
        results.append(num * multiplier)
    return results

print("\n=== REGULAR + *ARGS ===\n")
print(f"Multiply by 2: {multiply_by(2, 1, 2, 3, 4, 5)}")
print(f"Multiply by 10: {multiply_by(10, 5, 10, 15)}")

# Combining regular parameters with **kwargs
def create_profile(name, **details):
    profile = {'name': name}
    profile.update(details)
    return profile

print("\n=== REGULAR + **KWARGS ===\n")
user1 = create_profile("Alice", age=25, city="New York", email="alice@example.com")
user2 = create_profile("Bob", age=30, occupation="Engineer")
print(user1)
print(user2)

# Combining *args and **kwargs
def full_function(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print("\n=== *ARGS AND **KWARGS ===\n")
full_function(1, 2, 3, name="Alice", age=25)

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Calculate average
def calculate_average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(f"Average of 10, 20, 30: {calculate_average(10, 20, 30)}")
print(f"Average of 5, 10, 15, 20, 25: {calculate_average(5, 10, 15, 20, 25)}")

# Example 2: Find maximum
def find_maximum(*args):
    if not args:
        return None
    return max(args)

print(f"\nMax of 3, 7, 2, 9, 1: {find_maximum(3, 7, 2, 9, 1)}")

# Example 3: Join strings
def join_strings(separator=" ", *strings):
    return separator.join(strings)

print(f"\nJoin with space: {join_strings(' ', 'Hello', 'World', 'Python')}")
print(f"Join with comma: {join_strings(', ', 'apple', 'banana', 'cherry')}")

# Example 4: Build URL
def build_url(base, **params):
    url = base
    if params:
        query_parts = [f"{k}={v}" for k, v in params.items()]
        url += "?" + "&".join(query_parts)
    return url

print("\nURL Building:")
print(build_url("https://example.com/api"))
print(build_url("https://example.com/search", q="python", page=1, limit=10))

# Example 5: Format message
def format_message(template, **values):
    return template.format(**values)

message = format_message(
    "Hello {name}, you are {age} years old.",
    name="Alice",
    age=25
)
print(f"\nFormatted message: {message}")

# Example 6: Database-like insert
def insert_record(table, **fields):
    print(f"INSERT INTO {table}")
    for key, value in fields.items():
        print(f"  {key} = {value}")

print("\nDatabase Insert:")
insert_record("users", username="alice", email="alice@example.com", age=25)

# Example 7: Log with metadata
def log(*messages, **metadata):
    print(" ".join(str(m) for m in messages))
    if metadata:
        print(f"  Metadata: {metadata}")

print("\nLogging:")
log("User", "logged", "in", user_id=123, ip="192.168.1.1")

# Example 8: Unpacking into *args and **kwargs
def display_all(*args, **kwargs):
    print(f"Args count: {len(args)}")
    print(f"Kwargs count: {len(kwargs)}")
    print(f"All args: {args}")
    print(f"All kwargs: {kwargs}")

print("\nDisplay All:")
values = [1, 2, 3]
options = {'key': 'value', 'name': 'test'}
display_all(*values, **options)
