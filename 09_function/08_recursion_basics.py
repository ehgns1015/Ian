"""
Recursion - Basics

Recursion is when a function calls itself.
Every recursive function needs:
1. Base case - condition to stop recursion
2. Recursive case - function calls itself with modified input

Source: 04_recursive_functions.docx - Recursion Basics
"""

# Basic recursion - countdown
def countdown(n):
    # Base case
    if n <= 0:
        print("Done!")
        return

    # Recursive case
    print(n)
    countdown(n - 1)

print("=== COUNTDOWN ===\n")
countdown(5)

# Count up recursively
def count_up(current, limit):
    # Base case
    if current > limit:
        return

    # Recursive case
    print(current)
    count_up(current + 1, limit)

print("\n=== COUNT UP ===\n")
count_up(1, 5)

# Sum of numbers from 1 to n
def sum_to_n(n):
    # Base case
    if n == 1:
        return 1

    # Recursive case
    return n + sum_to_n(n - 1)

print("\n=== SUM TO N ===\n")
print(f"Sum 1 to 5: {sum_to_n(5)}")
print(f"Sum 1 to 10: {sum_to_n(10)}")

# Factorial (n!)
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)

print("\n=== FACTORIAL ===\n")
print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")

# Power function (x^n)
def power(x, n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return x * power(x, n - 1)

print("\n=== POWER ===\n")
print(f"2^3 = {power(2, 3)}")
print(f"5^4 = {power(5, 4)}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Sum of list
def sum_list(numbers):
    # Base case: empty list
    if not numbers:
        return 0

    # Recursive case: first element + sum of rest
    return numbers[0] + sum_list(numbers[1:])

nums = [1, 2, 3, 4, 5]
print(f"Sum of {nums}: {sum_list(nums)}")

# Example 2: Find maximum in list
def find_max(numbers):
    # Base case: single element
    if len(numbers) == 1:
        return numbers[0]

    # Recursive case
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

nums = [3, 7, 2, 9, 1, 5]
print(f"\nMax of {nums}: {find_max(nums)}")

# Example 3: Count digits
def count_digits(n):
    # Base case
    if n == 0:
        return 0

    # Recursive case
    return 1 + count_digits(n // 10)

print(f"\nDigits in 12345: {count_digits(12345)}")
print(f"Digits in 987: {count_digits(987)}")

# Example 4: Reverse string
def reverse_string(s):
    # Base case
    if len(s) <= 1:
        return s

    # Recursive case
    return s[-1] + reverse_string(s[:-1])

print(f"\nReverse 'hello': {reverse_string('hello')}")
print(f"Reverse 'python': {reverse_string('python')}")

# Example 5: Is palindrome
def is_palindrome(s):
    # Base case
    if len(s) <= 1:
        return True

    # Recursive case
    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])

print(f"\nIs 'radar' palindrome? {is_palindrome('radar')}")
print(f"Is 'hello' palindrome? {is_palindrome('hello')}")

# Visualization of recursion
print("\n=== RECURSION VISUALIZATION ===\n")

def factorial_verbose(n, indent=0):
    spacing = "  " * indent
    print(f"{spacing}factorial({n}) called")

    if n == 0 or n == 1:
        print(f"{spacing}Base case: returning 1")
        return 1

    result = n * factorial_verbose(n - 1, indent + 1)
    print(f"{spacing}Returning {n} * factorial({n-1}) = {result}")
    return result

print("Factorial(4) execution:")
factorial_verbose(4)

# Important concepts
print("\n=== RECURSION CONCEPTS ===\n")
print("1. Base Case: Condition to stop recursion (prevents infinite loop)")
print("2. Recursive Case: Function calls itself with modified input")
print("3. Stack: Each call is added to the call stack")
print("4. Return: Results bubble up through the stack")
print("\nWarning: Deep recursion can cause stack overflow!")
print("Python has a default recursion limit (usually 1000)")
