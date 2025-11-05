"""
Inheritance

Inheritance allows a class to inherit attributes and methods from another class.
The child class (subclass) inherits from the parent class (superclass).

Source: Object.docx - Section 3: Inheritance
"""

# Basic inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):  # Override parent method
        print("Meow")

class Dog(Animal):
    def speak(self):
        print("Woof")

print("=== BASIC INHERITANCE ===\n")

cat = Cat("Whiskers")
print(f"{cat.name} says: ", end="")
cat.speak()

dog = Dog("Buddy")
print(f"{dog.name} says: ", end="")
dog.speak()

# Inheritance with additional attributes
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"{self.year} {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)  # Call parent constructor
        self.doors = doors

    def info(self):
        super().info()  # Call parent method
        print(f"Doors: {self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, year, bike_type):
        super().__init__(brand, year)
        self.bike_type = bike_type

    def move(self):
        print(f"The {self.bike_type} bike is pedaling")

print("\n=== INHERITANCE WITH SUPER() ===\n")

car = Car("Toyota", 2020, 4)
car.info()

bike = Bike("Giant", 2021, "Mountain")
print(f"\n{bike.year} {bike.brand}")
bike.move()

# Multiple levels of inheritance
class LivingBeing:
    def breathe(self):
        print("Breathing...")

class Mammal(LivingBeing):
    def feed_milk(self):
        print("Feeding milk to young")

class Human(Mammal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is speaking")

print("\n=== MULTI-LEVEL INHERITANCE ===\n")

person = Human("Alice")
person.breathe()  # From LivingBeing
person.feed_milk()  # From Mammal
person.speak()  # From Human

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Employee hierarchy
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name}, Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display(self):
        super().display()
        print(f"Language: {self.language}")

print("Employee Hierarchy:")
mgr = Manager("Alice", 80000, "Engineering")
mgr.display()

print()
dev = Developer("Bob", 70000, "Python")
dev.display()

# Example 2: Shape hierarchy
class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f"A {self.color} shape")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def describe(self):
        super().describe()
        print(f"Circle with radius {self.radius}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        super().describe()
        print(f"Rectangle: {self.width} x {self.height}")

print("\nShapes:")
circle = Circle("red", 5)
circle.describe()
print(f"Area: {circle.area():.2f}\n")

rect = Rectangle("blue", 4, 6)
rect.describe()
print(f"Area: {rect.area()}")

# Method Resolution Order (MRO)
print("\n=== METHOD RESOLUTION ORDER ===\n")
print("MRO for Human:", [c.__name__ for c in Human.__mro__])

# Key concepts
print("\n=== KEY CONCEPTS ===\n")
print("Parent/Base/Super class: The class being inherited from")
print("Child/Derived/Sub class: The class that inherits")
print("super(): Function to call parent class methods")
print("Override: Child class replaces parent's method")
print("Extend: Child class adds to parent's behavior")
