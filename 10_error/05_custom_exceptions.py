"""
Custom Exceptions

You can create your own exception classes by inheriting from Exception.
Custom exceptions make code more readable and maintainable.

Source: Error Handling.docx - Custom Exceptions
"""

# Basic custom exception
class CustomError(Exception):
    pass

print("=== BASIC CUSTOM EXCEPTION ===\n")

def risky_operation():
    raise CustomError("Something went wrong")

try:
    risky_operation()
except CustomError as e:
    print(f"Caught custom error: {e}")

# Custom exception with message
class InvalidAgeError(Exception):
    def __init__(self, age, message="Invalid age provided"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.age}"

print("\n=== CUSTOM EXCEPTION WITH ATTRIBUTES ===\n")

def check_age(age):
    if age < 0:
        raise InvalidAgeError(age, "Age cannot be negative")
    if age > 150:
        raise InvalidAgeError(age, "Age too high")
    return True

try:
    check_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e}")
    print(f"Invalid age was: {e.age}")

# Multiple custom exceptions
print("\n=== MULTIPLE CUSTOM EXCEPTIONS ===\n")

class ValidationError(Exception):
    """Base class for validation errors"""
    pass

class EmailValidationError(ValidationError):
    """Raised when email is invalid"""
    pass

class PasswordValidationError(ValidationError):
    """Raised when password is invalid"""
    pass

class UsernameValidationError(ValidationError):
    """Raised when username is invalid"""
    pass

def validate_user(username, password, email):
    if len(username) < 3:
        raise UsernameValidationError("Username too short")

    if len(password) < 8:
        raise PasswordValidationError("Password too short")

    if "@" not in email:
        raise EmailValidationError("Invalid email format")

    return True

# Test validation
users = [
    ("alice", "password123", "alice@example.com"),
    ("ab", "password123", "alice@example.com"),
    ("alice", "pass", "alice@example.com"),
    ("alice", "password123", "invalid-email")
]

for username, password, email in users:
    try:
        validate_user(username, password, email)
        print(f"✓ Valid: {username}")
    except ValidationError as e:
        print(f"✗ Invalid: {username} - {type(e).__name__}: {e}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: E-commerce system
class InsufficientStockError(Exception):
    def __init__(self, product, requested, available):
        self.product = product
        self.requested = requested
        self.available = available
        message = f"Cannot fulfill order: {product} - Requested: {requested}, Available: {available}"
        super().__init__(message)

class InvalidPriceError(Exception):
    pass

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > self.stock:
            raise InsufficientStockError(self.name, quantity, self.stock)

        if self.price < 0:
            raise InvalidPriceError(f"Invalid price for {self.name}: {self.price}")

        self.stock -= quantity
        total = self.price * quantity
        return total

print("E-commerce Example:")
laptop = Product("Laptop", 999.99, 5)

try:
    total = laptop.purchase(3)
    print(f"Purchase successful: ${total:.2f}")
    print(f"Remaining stock: {laptop.stock}")
except (InsufficientStockError, InvalidPriceError, ValueError) as e:
    print(f"Purchase failed: {e}")

try:
    total = laptop.purchase(10)  # Not enough stock
except InsufficientStockError as e:
    print(f"\nPurchase failed: {e}")
    print(f"Product: {e.product}")
    print(f"Requested: {e.requested}")
    print(f"Available: {e.available}")

# Example 2: Banking system
print("\n=== BANKING SYSTEM ===")

class BankError(Exception):
    """Base exception for banking errors"""
    pass

class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance ${balance}, Requested ${amount}")

class InvalidAccountError(BankError):
    pass

class TransactionLimitError(BankError):
    pass

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.daily_limit = 1000

    def withdraw(self, amount):
        if amount > self.daily_limit:
            raise TransactionLimitError(f"Daily limit exceeded: ${self.daily_limit}")

        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)

        self.balance -= amount
        return self.balance

# Test banking operations
account = BankAccount("12345", 500)
print(f"Account: {account.account_number}, Balance: ${account.balance}")

transactions = [200, 150, 250, 1500]

for amount in transactions:
    try:
        new_balance = account.withdraw(amount)
        print(f"Withdrew ${amount}, New balance: ${new_balance}")
    except BankError as e:
        print(f"Transaction failed (${amount}): {type(e).__name__} - {e}")

# Example 3: Network exceptions
print("\n=== NETWORK EXCEPTIONS ===")

class NetworkError(Exception):
    """Base class for network errors"""
    pass

class ConnectionTimeoutError(NetworkError):
    pass

class ServerNotFoundError(NetworkError):
    pass

class AuthenticationError(NetworkError):
    pass

def connect_to_server(server, timeout=5, authenticated=True):
    if timeout < 1:
        raise ConnectionTimeoutError(f"Connection timeout: {timeout}s")

    if not server:
        raise ServerNotFoundError("Server address not provided")

    if not authenticated:
        raise AuthenticationError("Authentication required")

    return f"Connected to {server}"

# Test connections
connections = [
    ("server1.com", 10, True),
    ("server2.com", 0, True),
    ("", 5, True),
    ("server3.com", 5, False)
]

for server, timeout, auth in connections:
    try:
        result = connect_to_server(server, timeout, auth)
        print(f"✓ {result}")
    except NetworkError as e:
        print(f"✗ Connection failed: {type(e).__name__} - {e}")

# Exception hierarchy
print("\n=== CUSTOM EXCEPTION HIERARCHY ===\n")
print("Create base exception for your domain:")
print("class MyAppError(Exception):")
print("    pass")
print("\nDerived exceptions:")
print("class DatabaseError(MyAppError):")
print("    pass")
print("class APIError(MyAppError):")
print("    pass")
print("\nBenefits:")
print("- Catch all related errors: except MyAppError")
print("- Catch specific errors: except DatabaseError")
print("- Clear error hierarchy and organization")
