"""
The __init__ Method (Constructor)

__init__ is a special method called when an object is created.
It initializes the object's attributes.

Source: Object.docx - Section 1: Constructor
"""
from math import pi, pow

# Basic constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person object created: {name}")

print("=== BASIC CONSTRUCTOR ===\n")

p1 = Person("Alice", 25)
print(f"Name: {p1.name}, Age: {p1.age}")

# Constructor with default values
class Product:
    def __init__(self, name, price=0, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

print("\n=== DEFAULT VALUES ===\n")

prod1 = Product("Laptop", 999.99, 5)
print(f"{prod1.name}: ${prod1.price} x {prod1.quantity}")

prod2 = Product("Mouse")
print(f"{prod2.name}: ${prod2.price} x {prod2.quantity}")

# Constructor with validation
class User:
    def __init__(self, username, email):
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if "@" not in email:
            raise ValueError("Invalid email")

        self.username = username
        self.email = email

print("\n=== VALIDATION IN CONSTRUCTOR ===\n")

try:
    user1 = User("alice", "alice@example.com")
    print(f"Created user: {user1.username}")

    user2 = User("ab", "invalid")  # This will fail
except ValueError as e:
    print(f"Error: {e}")

# Constructor with calculated attributes
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = pi * pow(radius, 2)
        self.circumference = 2 * pi * radius

print("\n=== CALCULATED ATTRIBUTES ===\n")

circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area:.2f}")
print(f"Circumference: {circle.circumference:.2f}")

# Constructor calling other methods
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.calculate_annual()  # Call method in constructor

    def calculate_annual(self):
        self.annual_salary = self.salary * 12

print("\n=== CALLING METHODS IN CONSTRUCTOR ===\n")

emp = Employee("Ian", 5000)
print(f"{emp.name}: Monthly ${emp.salary}, Annual ${emp.annual_salary}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
        print("Shopping cart created")

    def add_item(self, item, price):
        self.items.append(item)
        self.total += price
        print(f"Added {item}: ${price}")

cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 29.99)
print(f"Total: ${cart.total:.2f}")

# Example 2: Temperature Sensor
class TemperatureSensor:
    def __init__(self, location, unit="Celsius"):
        self.location = location
        self.unit = unit
        self.readings = []
        print(f"Sensor initialized at {location} ({unit})")

    def add_reading(self, temp):
        self.readings.append(temp)

    def get_average(self):
        if not self.readings:
            return 0
        return sum(self.readings) / len(self.readings)

sensor = TemperatureSensor("Room A")
sensor.add_reading(22.5)
sensor.add_reading(23.0)
sensor.add_reading(22.8)
print(f"Average temperature: {sensor.get_average():.1f}°{sensor.unit}")

# Example 3: Account with timestamp
from datetime import datetime

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.created_at = datetime.now()

    def display_info(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance}")
        print(f"Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

print("\nAccount with timestamp:")
account = Account("Alice", 1000)
account.display_info()

# Constructor best practices
print("\n=== CONSTRUCTOR BEST PRACTICES ===\n")
print("1. Initialize all instance attributes")
print("2. Validate input parameters")
print("3. Use default parameter values when appropriate")
print("4. Keep constructor simple")
print("5. Don't do heavy computation in __init__")
print("6. Consider using @classmethod for alternative constructors")
