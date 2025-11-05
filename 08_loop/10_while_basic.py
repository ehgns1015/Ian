"""
While Loop - Basic

The while loop continues to execute as long as a condition is True.
Unlike for loops which iterate over sequences, while loops are condition-based.

Syntax: while condition:
            # code block

Source: 02_while_loops.docx - Introduction to While Loops
"""

# Basic while loop
print("=== BASIC WHILE LOOP ===\n")

count = 0
while count < 5:
    print(count)
    count += 1

# While loop with countdown
print("\n=== COUNTDOWN ===\n")

number = 5
while number > 0:
    print(number)
    number -= 1
print("Done!")

# While loop with increment
print("\n=== SUM OF NUMBERS ===\n")

total = 0
num = 1
while num <= 10:
    total += num
    num += 1

print(f"Sum of 1 to 10: {total}")

# While loop with user-defined end
print("\n=== WHILE WITH CONDITION ===\n")

balance = 100
withdrawal = 15

print(f"Starting balance: ${balance}")
while balance >= withdrawal:
    balance -= withdrawal
    print(f"Withdrew ${withdrawal}, Remaining: ${balance}")

print(f"Final balance: ${balance}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Find first power of 2 greater than n
n = 100
power = 1

while power <= n:
    power *= 2

print(f"First power of 2 greater than {n}: {power}")

# Example 2: Count digits
number = 12345
digits = 0

temp = number
while temp > 0:
    temp //= 10
    digits += 1

print(f"Number {number} has {digits} digits")

# Example 3: Reverse a number
number = 12345
reversed_num = 0

temp = number
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

print(f"Original: {number}")
print(f"Reversed: {reversed_num}")

# Example 4: Find factorial
n = 5
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"{n}! = {factorial}")

# Example 5: Double until threshold
value = 1
threshold = 1000

print(f"\nDoubling {value} until it exceeds {threshold}:")
while value <= threshold:
    print(value)
    value *= 2

# Example 6: Password attempts
print("\n=== PASSWORD ATTEMPTS ===")
correct_password = "secret"
attempts = 0
max_attempts = 3

# Simulated attempts (in real scenario, use input())
test_passwords = ["wrong1", "wrong2", "secret"]
attempt_index = 0

while attempts < max_attempts:
    password = test_passwords[attempt_index]
    print(f"Attempt {attempts + 1}: {password}")

    if password == correct_password:
        print("Access granted!")
        break

    attempts += 1
    attempt_index += 1
else:
    print("Access denied: Maximum attempts reached")

# Example 7: Calculate GCD (Greatest Common Divisor)
print("\n=== GCD CALCULATION ===")
a, b = 48, 18
orig_a, orig_b = a, b

while b != 0:
    temp = b
    b = a % b
    a = temp

print(f"GCD of {orig_a} and {orig_b}: {a}")

# Example 8: Generate sequence
print("\n=== FIBONACCI SEQUENCE ===")
a, b = 0, 1
max_value = 100

print(f"Fibonacci numbers up to {max_value}:")
while a <= max_value:
    print(a, end=" ")
    a, b = b, a + b
print()

# Example 9: Collect items until condition
print("\n=== COLLECT ITEMS ===")
numbers = []
current = 1

while len(numbers) < 5:
    numbers.append(current)
    current += 2

print(f"Collected odd numbers: {numbers}")

# Example 10: While with multiple conditions
print("\n=== MULTIPLE CONDITIONS ===")
x = 0
y = 10

while x < 5 and y > 5:
    print(f"x={x}, y={y}")
    x += 1
    y -= 1

print(f"Final: x={x}, y={y}")

# Example 11: Process until flag changes
print("\n=== PROCESS WITH FLAG ===")
is_processing = True
items_processed = 0
max_items = 5

while is_processing:
    items_processed += 1
    print(f"Processing item {items_processed}")

    if items_processed >= max_items:
        is_processing = False

print(f"Total items processed: {items_processed}")

# Example 12: Halving until below threshold
print("\n=== HALVING PROCESS ===")
value = 1000
threshold = 10

print(f"Halving {value} until below {threshold}:")
while value >= threshold:
    print(f"{value:.2f}")
    value /= 2

print(f"Final value: {value:.2f}")
