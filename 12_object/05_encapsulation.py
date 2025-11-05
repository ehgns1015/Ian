"""
Encapsulation

Encapsulation restricts direct access to some of an object's components.
Private variables (prefix with __) can only be accessed within the class.
Use getter and setter methods to control access.

Source: Object.docx - Section 4: Encapsulation
"""

# Basic encapsulation with private variables
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable (name mangling)

    def get_balance(self):  # Getter
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Amount must be positive")

print("=== BASIC ENCAPSULATION ===\n")

acc = BankAccount(1000)
print(f"Initial balance: ${acc.get_balance()}")
acc.deposit(500)
print(f"New balance: ${acc.get_balance()}")
acc.withdraw(200)
print(f"Final balance: ${acc.get_balance()}")

# Cannot access private variable directly
print(f"\nTrying to access __balance directly...")
try:
    print(acc.__balance)  # This won't work
except AttributeError as e:
    print(f"Error: {e}")

# Protected variable (single underscore)
class Person:
    def __init__(self, name, age):
        self._name = name  # Protected (convention)
        self.__age = age  # Private

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 150:
            self.__age = age
        else:
            print("Invalid age")

print("\n=== PROTECTED VS PRIVATE ===\n")

person = Person("Alice", 25)
print(f"Name (protected): {person._name}")  # Accessible but shouldn't be used
print(f"Age (via getter): {person.get_age()}")

person.set_age(30)
print(f"Updated age: {person.get_age()}")

person.set_age(200)  # Invalid

# Property decorator (Pythonic approach)
class Student:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    @property  # Getter
    def score(self):
        return self._score

    @score.setter  # Setter
    def score(self, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            raise ValueError("Score must be between 0 and 100")

print("\n=== PROPERTY DECORATOR ===\n")

student = Student("Bob", 85)
print(f"Score: {student.score}")  # Accessed like an attribute

student.score = 95  # Set like an attribute
print(f"Updated score: {student.score}")

try:
    student.score = 150  # Invalid
except ValueError as e:
    print(f"Error: {e}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Temperature class
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:  # Absolute zero
            raise ValueError("Temperature below absolute zero")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

print("Temperature Class:")
temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")

temp.celsius = 0
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 100
print(f"{temp.celsius:.1f}°C = {temp.fahrenheit}°F")

# Example 2: User with password
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = self.__hash_password(password)

    def __hash_password(self, password):
        # Simplified hashing (in real app, use proper hashing)
        return f"hashed_{password}"

    def check_password(self, password):
        return self.__password == self.__hash_password(password)

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = self.__hash_password(new_password)
            print("Password changed successfully")
        else:
            print("Incorrect old password")

print("\nUser Authentication:")
user = User("alice", "secret123")
print(f"Username: {user.username}")

print(f"Check password 'secret123': {user.check_password('secret123')}")
print(f"Check password 'wrong': {user.check_password('wrong')}")

user.change_password("secret123", "newsecret456")

# Example 3: Circle with validation
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self.__radius = value

    @property
    def area(self):
        return 3.14159 * self.__radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self.__radius

print("\nCircle with Encapsulation:")
circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area:.2f}")
print(f"Circumference: {circle.circumference:.2f}")

circle.radius = 10
print(f"\nNew radius: {circle.radius}")
print(f"New area: {circle.area:.2f}")

# Benefits of encapsulation
print("\n=== BENEFITS OF ENCAPSULATION ===\n")
print("1. Data Protection: Prevent invalid state")
print("2. Flexibility: Change internal implementation")
print("3. Validation: Control how data is set")
print("4. Read-only properties: Computed values")
print("5. Debugging: Track value changes")
