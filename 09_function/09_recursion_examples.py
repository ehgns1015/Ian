"""
Recursion - Advanced Examples

More complex recursive algorithms including:
- Fibonacci sequence
- Binary search
- Tree traversal concepts
- String permutations

Source: 04_recursive_functions.docx - Recursion Examples
"""

# Fibonacci sequence
def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print("=== FIBONACCI SEQUENCE ===\n")
print("First 10 Fibonacci numbers:")
for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")

# GCD (Greatest Common Divisor)
def gcd(a, b):
    # Base case
    if b == 0:
        return a

    # Recursive case (Euclidean algorithm)
    return gcd(b, a % b)

print("\n=== GREATEST COMMON DIVISOR ===\n")
print(f"GCD(48, 18) = {gcd(48, 18)}")
print(f"GCD(100, 35) = {gcd(100, 35)}")

# Binary search (recursive)
def binary_search(arr, target, left, right):
    # Base case: not found
    if left > right:
        return -1

    mid = (left + right) // 2

    # Base case: found
    if arr[mid] == target:
        return mid

    # Recursive cases
    if arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

print("\n=== BINARY SEARCH ===\n")
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13

index = binary_search(sorted_list, target, 0, len(sorted_list) - 1)
print(f"List: {sorted_list}")
print(f"Finding {target}: Index {index}")

# Sum of digits
def sum_of_digits(n):
    # Base case
    if n == 0:
        return 0

    # Recursive case
    return (n % 10) + sum_of_digits(n // 10)

print("\n=== SUM OF DIGITS ===\n")
print(f"Sum of digits in 12345: {sum_of_digits(12345)}")
print(f"Sum of digits in 9876: {sum_of_digits(9876)}")

# Count occurrences in list
def count_occurrences(lst, target):
    # Base case: empty list
    if not lst:
        return 0

    # Recursive case
    count = 1 if lst[0] == target else 0
    return count + count_occurrences(lst[1:], target)

print("\n=== COUNT OCCURRENCES ===\n")
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"List: {numbers}")
print(f"Count of 2: {count_occurrences(numbers, 2)}")

# Flatten nested list
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print("\n=== FLATTEN NESTED LIST ===\n")
nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"Nested: {nested}")
print(f"Flattened: {flatten(nested)}")

# String permutations
def permutations(s):
    # Base case
    if len(s) <= 1:
        return [s]

    # Recursive case
    perms = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for perm in permutations(remaining):
            perms.append(char + perm)

    return perms

print("\n=== STRING PERMUTATIONS ===\n")
word = "abc"
perms = permutations(word)
print(f"Permutations of '{word}': {perms}")

# Calculate power with optimization
def power_optimized(base, exp):
    # Base cases
    if exp == 0:
        return 1
    if exp == 1:
        return base

    # Recursive case with optimization
    if exp % 2 == 0:
        half = power_optimized(base, exp // 2)
        return half * half
    else:
        return base * power_optimized(base, exp - 1)

print("\n=== OPTIMIZED POWER ===\n")
print(f"2^10 = {power_optimized(2, 10)}")
print(f"3^7 = {power_optimized(3, 7)}")

# Tower of Hanoi
def tower_of_hanoi(n, source, destination, auxiliary, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination, moves)

    # Move the largest disk
    moves.append(f"Move disk {n} from {source} to {destination}")

    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source, moves)

print("\n=== TOWER OF HANOI ===\n")
moves = []
n = 3
tower_of_hanoi(n, 'A', 'C', 'B', moves)
print(f"Moves for {n} disks:")
for i, move in enumerate(moves, 1):
    print(f"{i}. {move}")

# Generate subsets
def generate_subsets(lst):
    # Base case
    if not lst:
        return [[]]

    # Recursive case
    first = lst[0]
    rest_subsets = generate_subsets(lst[1:])

    new_subsets = []
    for subset in rest_subsets:
        new_subsets.append(subset)
        new_subsets.append([first] + subset)

    return new_subsets

print("\n=== GENERATE SUBSETS ===\n")
numbers = [1, 2, 3]
subsets = generate_subsets(numbers)
print(f"Subsets of {numbers}:")
for subset in subsets:
    print(f"  {subset}")

# Memoization example (optimized Fibonacci)
def fibonacci_memo(n, memo={}):
    # Check if already calculated
    if n in memo:
        return memo[n]

    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Calculate and store
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print("\n=== FIBONACCI WITH MEMOIZATION ===\n")
print("Larger Fibonacci numbers (optimized):")
for i in [10, 20, 30]:
    print(f"fib({i}) = {fibonacci_memo(i)}")

# Recursion depth
print("\n=== RECURSION TIPS ===\n")
print("1. Always define a base case to prevent infinite recursion")
print("2. Ensure recursive calls move toward the base case")
print("3. For large problems, consider iterative solutions")
print("4. Use memoization to optimize recursive algorithms")
print("5. Python's default recursion limit is around 1000")
print("6. Recursion uses more memory (stack space)")
