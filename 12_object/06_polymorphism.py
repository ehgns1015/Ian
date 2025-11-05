"""
Polymorphism

Polymorphism means "many forms".
Different classes can have methods with the same name but different implementations.
Objects of different classes can be treated uniformly.

Source: Object.docx - Section 5: Polymorphism
"""

# Basic polymorphism
class Bird:
    def make_sound(self):
        print("Tweet")

class Dog:
    def make_sound(self):
        print("Bark")

class Cat:
    def make_sound(self):
        print("Meow")

print("=== BASIC POLYMORPHISM ===\n")

animals = [Bird(), Dog(), Cat()]

for animal in animals:
    animal.make_sound()  # Same method name, different behavior

# Polymorphism with inheritance
class Animal:
    def speak(self):
        pass

class Cow(Animal):
    def speak(self):
        print("Moo")

class Sheep(Animal):
    def speak(self):
        print("Baa")

class Duck(Animal):
    def speak(self):
        print("Quack")

print("\n=== POLYMORPHISM WITH INHERITANCE ===\n")

def animal_sound(animal):
    animal.speak()

cow = Cow()
sheep = Sheep()
duck = Duck()

animal_sound(cow)
animal_sound(sheep)
animal_sound(duck)

# Polymorphism with different parameter types
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

print("\n=== POLYMORPHISM WITH SHAPES ===\n")

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")

# Duck typing (Python's approach to polymorphism)
class FileReader:
    def read(self):
        return "Reading from file..."

class DatabaseReader:
    def read(self):
        return "Reading from database..."

class APIReader:
    def read(self):
        return "Reading from API..."

print("\n=== DUCK TYPING ===\n")

def process_data(reader):
    # Don't care about type, just that it has read() method
    data = reader.read()
    print(data)

process_data(FileReader())
process_data(DatabaseReader())
process_data(APIReader())

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Payment methods
class Payment:
    def process(self, amount):
        pass

class CreditCard(Payment):
    def process(self, amount):
        print(f"Processing ${amount} via Credit Card")

class PayPal(Payment):
    def process(self, amount):
        print(f"Processing ${amount} via PayPal")

class Bitcoin(Payment):
    def process(self, amount):
        print(f"Processing ${amount} via Bitcoin")

def checkout(payment_method, amount):
    payment_method.process(amount)

print("Checkout Process:")
checkout(CreditCard(), 99.99)
checkout(PayPal(), 149.50)
checkout(Bitcoin(), 0.005)

# Example 2: File formatters
class Formatter:
    def format(self, data):
        pass

class JSONFormatter(Formatter):
    def format(self, data):
        return f"JSON: {data}"

class XMLFormatter(Formatter):
    def format(self, data):
        return f"<data>{data}</data>"

class CSVFormatter(Formatter):
    def format(self, data):
        return f"CSV: {','.join(map(str, data))}"

print("\nData Formatting:")
data = ["Alice", 25, "NYC"]

formatters = [JSONFormatter(), XMLFormatter(), CSVFormatter()]

for formatter in formatters:
    print(formatter.format(data))

# Example 3: Notification system
class Notifier:
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Email: {message}")

class SMSNotifier(Notifier):
    def send(self, message):
        print(f"SMS: {message}")

class PushNotifier(Notifier):
    def send(self, message):
        print(f"Push notification: {message}")

def notify_users(notifiers, message):
    for notifier in notifiers:
        notifier.send(message)

print("\nNotification System:")
notifiers = [EmailNotifier(), SMSNotifier(), PushNotifier()]
notify_users(notifiers, "Your order has been shipped!")

# Polymorphism with operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

print("\nOperator Overloading:")
v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2  # Uses __add__ method
print(f"{v1} + {v2} = {v3}")

# Benefits of polymorphism
print("\n=== BENEFITS OF POLYMORPHISM ===\n")
print("1. Flexibility: Write code that works with different types")
print("2. Extensibility: Add new classes without changing existing code")
print("3. Clean code: Treat different objects uniformly")
print("4. Maintainability: Easier to update and extend")
