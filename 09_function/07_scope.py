"""
Variable Scope

Scope determines where variables are accessible in your code.
Python has four scopes: Local, Enclosing, Global, and Built-in (LEGB Rule)

Source: 03_function.docx - Scope
"""

# Global scope
global_var = "I am global"

def display_global():
    print(global_var)

print("=== GLOBAL SCOPE ===\n")
print(global_var)
display_global()

# Local scope
def local_example():
    local_var = "I am local"
    print(local_var)

print("\n=== LOCAL SCOPE ===\n")
local_example()
# print(local_var)  # This would cause an error - local_var not accessible here

# Accessing global from local
counter = 0

def increment():
    global counter  # Declare we're using the global variable
    counter += 1
    print(f"Counter: {counter}")

print("\n=== MODIFYING GLOBAL ===\n")
print(f"Initial counter: {counter}")
increment()
increment()
increment()

# Local variable shadows global
name = "Global Name"

def show_name():
    name = "Local Name"  # This creates a new local variable
    print(f"Inside function: {name}")

print("\n=== VARIABLE SHADOWING ===\n")
print(f"Before function: {name}")
show_name()
print(f"After function: {name}")  # Global unchanged

# Enclosing scope (nested functions)
def outer():
    outer_var = "I am in outer"

    def inner():
        print(f"Inner accessing: {outer_var}")

    inner()

print("\n=== ENCLOSING SCOPE ===\n")
outer()

# nonlocal keyword
def counter_func():
    count = 0

    def increment():
        nonlocal count  # Refer to enclosing scope variable
        count += 1
        return count

    print(f"Count: {increment()}")
    print(f"Count: {increment()}")
    print(f"Count: {increment()}")

print("\n=== NONLOCAL KEYWORD ===\n")
counter_func()

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Function with global configuration
CONFIG = {
    'debug': False,
    'max_retries': 3
}

def process_request():
    if CONFIG['debug']:
        print("Debug mode: Processing request")
    print(f"Max retries: {CONFIG['max_retries']}")

process_request()

# Example 2: Counter with closure
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

print("\nCounter with Closure:")
counter1 = make_counter()
print(f"Counter1: {counter1()}")
print(f"Counter1: {counter1()}")
print(f"Counter1: {counter1()}")

counter2 = make_counter()
print(f"Counter2: {counter2()}")
print(f"Counter2: {counter2()}")

# Example 3: Global state management
total_sales = 0

def add_sale(amount):
    global total_sales
    total_sales += amount
    print(f"Sale added: ${amount}, Total: ${total_sales}")

print("\nSales Tracking:")
add_sale(100)
add_sale(250)
add_sale(75)

# Example 4: Function factory
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

print("\nFunction Factory:")
times_2 = multiplier(2)
times_3 = multiplier(3)
times_10 = multiplier(10)

print(f"5 * 2 = {times_2(5)}")
print(f"5 * 3 = {times_3(5)}")
print(f"5 * 10 = {times_10(5)}")

# Example 5: Nested scope example
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

print("\nNested Scope:")
add_5 = outer_function(5)
add_10 = outer_function(10)

print(f"add_5(3) = {add_5(3)}")
print(f"add_10(3) = {add_10(3)}")

# LEGB Rule demonstration
x = "global x"

def test_legb():
    x = "local x"

    def inner():
        x = "inner local x"
        print(f"Inner: {x}")

    inner()
    print(f"Test function: {x}")

print("\n=== LEGB RULE ===\n")
print(f"Global: {x}")
test_legb()
print(f"Global after function: {x}")

# Best practices
print("\n=== SCOPE BEST PRACTICES ===\n")
print("1. Minimize use of global variables")
print("2. Pass data through parameters instead")
print("3. Return values instead of modifying globals")
print("4. Use local variables when possible")
print("5. Be cautious with variable shadowing")
