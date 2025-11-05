"""
Class Methods and Static Methods

Class methods: Use @classmethod decorator, receive class as first parameter (cls)
Static methods: Use @staticmethod decorator, don't receive self or cls
Instance methods: Regular methods that receive self

Source: Object.docx - Section 7: Class vs Static Methods
"""

# Static methods
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

print("=== STATIC METHODS ===\n")

# Call without creating instance
print(f"5 + 3 = {MathUtils.add(5, 3)}")
print(f"5 * 3 = {MathUtils.multiply(5, 3)}")

# Class methods
class Person:
    population = 0  # Class variable

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def describe(cls):
        print(f"This is class {cls.__name__}")
        print(f"Population: {cls.population}")

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # Alternative constructor
        age = 2024 - birth_year
        return cls(name)

print("\n=== CLASS METHODS ===\n")

Person.describe()

person1 = Person("Alice")
person2 = Person("Bob")

Person.describe()

# Using class method as alternative constructor
person3 = Person.from_birth_year("Charlie", 1990)
print(f"Created {person3.name}")

# All three method types together
class Employee:
    company_name = "TechCorp"  # Class variable

    def __init__(self, name, salary):
        self.name = name  # Instance variable
        self.salary = salary

    # Instance method
    def display_info(self):
        print(f"{self.name}: ${self.salary}")

    # Class method
    @classmethod
    def set_company(cls, name):
        cls.company_name = name

    @classmethod
    def from_monthly(cls, name, monthly_salary):
        return cls(name, monthly_salary * 12)

    # Static method
    @staticmethod
    def is_workday(day):
        return day not in ['Saturday', 'Sunday']

print("\n=== ALL METHOD TYPES ===\n")

# Instance method
emp = Employee("Alice", 60000)
emp.display_info()

# Class method
Employee.set_company("NewTech")
print(f"Company: {Employee.company_name}")

emp2 = Employee.from_monthly("Bob", 5000)
emp2.display_info()

# Static method
print(f"Is Monday a workday? {Employee.is_workday('Monday')}")
print(f"Is Saturday a workday? {Employee.is_workday('Saturday')}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Date class
from datetime import datetime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    @classmethod
    def today(cls):
        now = datetime.now()
        return cls(now.year, now.month, now.day)

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print("Date Class:")
date1 = Date(2024, 12, 25)
print(f"Date 1: {date1}")

date2 = Date.today()
print(f"Today: {date2}")

date3 = Date.from_string("2024-01-15")
print(f"From string: {date3}")

print(f"Is 2024 leap year? {Date.is_leap_year(2024)}")

# Example 2: Temperature converter
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @classmethod
    def describe(cls):
        print(f"{cls.__name__}: Convert temperatures between units")

print("\nTemperature Converter:")
TemperatureConverter.describe()

c = 25
f = TemperatureConverter.celsius_to_fahrenheit(c)
k = TemperatureConverter.celsius_to_kelvin(c)

print(f"{c}°C = {f}°F = {k}K")

# Example 3: Counter with class method
class Counter:
    count = 0

    def __init__(self):
        Counter.increment()

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def reset(cls):
        cls.count = 0

    @classmethod
    def get_count(cls):
        return cls.count

print("\nCounter:")
print(f"Initial count: {Counter.get_count()}")

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(f"After creating 3 objects: {Counter.get_count()}")

Counter.reset()
print(f"After reset: {Counter.get_count()}")

# When to use each type
print("\n=== WHEN TO USE EACH TYPE ===\n")

print("Instance methods:")
print("  - Operate on instance data (self)")
print("  - Access instance variables")
print("  - Most common method type")

print("\nClass methods (@classmethod):")
print("  - Operate on class data (cls)")
print("  - Alternative constructors")
print("  - Modify class state")
print("  - Factory methods")

print("\nStatic methods (@staticmethod):")
print("  - Don't need instance or class data")
print("  - Utility functions")
print("  - Logical grouping")
print("  - Pure functions related to class")
