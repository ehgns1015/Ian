"""
Raising Exceptions

You can raise exceptions manually using the raise keyword.
Useful for input validation, enforcing rules, or signaling errors.

Source: Error Handling.docx - Raising Exceptions
"""

# Basic raise
print("=== BASIC RAISE ===\n")

def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive")
    return number

try:
    result = check_positive(10)
    print(f"Valid: {result}")

    result = check_positive(-5)
    print(f"Valid: {result}")
except ValueError as e:
    print(f"Error: {e}")

# Raise different exception types
print("\n=== DIFFERENT EXCEPTION TYPES ===\n")

def divide(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("First argument must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    print(divide(10, 2))
    print(divide(10, "abc"))
except TypeError as e:
    print(f"TypeError: {e}")

# Raise with custom message
print("\n=== CUSTOM MESSAGES ===\n")

def validate_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative (got {age})")
    if age > 150:
        raise ValueError(f"Age too high (got {age})")
    if not isinstance(age, int):
        raise TypeError(f"Age must be integer (got {type(age).__name__})")
    return True

ages_to_test = [25, -5, 200, "abc"]

for age in ages_to_test:
    try:
        validate_age(age)
        print(f"Age {age}: Valid")
    except (ValueError, TypeError) as e:
        print(f"Age {age}: {e}")

# Re-raising exceptions
print("\n=== RE-RAISING EXCEPTIONS ===\n")

def process_data(data):
    try:
        result = int(data) / 10
        return result
    except ValueError:
        print("Logging: ValueError occurred")
        raise  # Re-raise the same exception

try:
    process_data("abc")
except ValueError:
    print("Caught re-raised exception")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: User registration validation
def register_user(username, password, email):
    if len(username) < 3:
        raise ValueError("Username must be at least 3 characters")

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")

    if "@" not in email:
        raise ValueError("Invalid email format")

    return {"username": username, "email": email}

print("User Registration:")
try:
    user1 = register_user("alice", "password123", "alice@example.com")
    print(f"Success: {user1['username']}")
except ValueError as e:
    print(f"Registration failed: {e}")

try:
    user2 = register_user("ab", "pass", "invalid")
    print(f"Success: {user2['username']}")
except ValueError as e:
    print(f"Registration failed: {e}")

# Example 2: Bank account operations
print("\n=== BANK ACCOUNT ===")

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: ${self.balance} < ${amount}"
            )
        self.balance -= amount
        return self.balance

account = BankAccount(1000)

try:
    print(f"Balance: ${account.balance}")
    account.withdraw(500)
    print(f"After withdrawal: ${account.balance}")
    account.withdraw(700)  # This will fail
except InsufficientFundsError as e:
    print(f"Error: {e}")

# Example 3: Configuration validator
print("\n=== CONFIGURATION VALIDATOR ===")

def validate_config(config):
    required_keys = ['host', 'port', 'database']

    for key in required_keys:
        if key not in config:
            raise KeyError(f"Missing required config key: '{key}'")

    if not isinstance(config['port'], int):
        raise TypeError("Port must be an integer")

    if config['port'] < 1 or config['port'] > 65535:
        raise ValueError(f"Invalid port number: {config['port']}")

    return True

configs = [
    {'host': 'localhost', 'port': 5432, 'database': 'mydb'},
    {'host': 'localhost', 'port': 5432},  # Missing 'database'
    {'host': 'localhost', 'port': '5432', 'database': 'mydb'},  # Wrong type
    {'host': 'localhost', 'port': 99999, 'database': 'mydb'}  # Invalid port
]

for i, config in enumerate(configs, 1):
    try:
        validate_config(config)
        print(f"Config {i}: Valid")
    except (KeyError, TypeError, ValueError) as e:
        print(f"Config {i}: {type(e).__name__} - {e}")

# Example 4: API response handler
print("\n=== API RESPONSE HANDLER ===")

def handle_api_response(status_code, data):
    if status_code == 200:
        return data
    elif status_code == 404:
        raise FileNotFoundError("Resource not found")
    elif status_code == 401:
        raise PermissionError("Unauthorized access")
    elif status_code == 500:
        raise RuntimeError("Server error")
    else:
        raise Exception(f"Unknown status code: {status_code}")

responses = [
    (200, {"data": "success"}),
    (404, None),
    (500, None)
]

for status, data in responses:
    try:
        result = handle_api_response(status, data)
        print(f"Status {status}: {result}")
    except Exception as e:
        print(f"Status {status}: {type(e).__name__} - {e}")

# When to raise exceptions
print("\n=== WHEN TO RAISE EXCEPTIONS ===\n")
print("Raise exceptions when:")
print("1. Input validation fails")
print("2. Preconditions are not met")
print("3. Invalid state is detected")
print("4. Business rules are violated")
print("5. Resources are unavailable")
print("\nDon't use exceptions for:")
print("1. Normal control flow")
print("2. Expected conditions")
print("3. Performance-critical code")
