"""
Object Composition

Composition is a "has-a" relationship between objects.
One class contains instances of other classes as attributes.
Promotes code reuse and flexibility.

Source: Object.docx - Section 8: Object Composition
"""

# Basic composition
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def start(self):
        print("Starting car...")
        self.engine.start()
        print("Car is running")

    def stop(self):
        print("Stopping car...")
        self.engine.stop()
        print("Car is off")

print("=== BASIC COMPOSITION ===\n")

car = Car()
car.start()
print()
car.stop()

# Composition vs Inheritance
print("\n=== COMPOSITION VS INHERITANCE ===\n")

# Inheritance: "is-a" relationship
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):  # Dog IS-A Animal
    def bark(self):
        print("Woof!")

# Composition: "has-a" relationship
class Tail:
    def wag(self):
        print("Wagging tail")

class DogComposition:
    def __init__(self):
        self.tail = Tail()  # Dog HAS-A Tail

    def be_happy(self):
        self.tail.wag()

dog = DogComposition()
dog.be_happy()

# Multiple composition
class CPU:
    def __init__(self, model):
        self.model = model

    def process(self):
        print(f"{self.model}: Processing data")

class RAM:
    def __init__(self, size):
        self.size = size

    def load(self):
        print(f"{self.size}GB RAM: Loading data")

class Storage:
    def __init__(self, capacity):
        self.capacity = capacity

    def read(self):
        print(f"{self.capacity}GB Storage: Reading data")

class Computer:
    def __init__(self, cpu_model, ram_size, storage_capacity):
        self.cpu = CPU(cpu_model)
        self.ram = RAM(ram_size)
        self.storage = Storage(storage_capacity)

    def run_program(self):
        print("Running program:")
        self.storage.read()
        self.ram.load()
        self.cpu.process()

print("\n=== MULTIPLE COMPOSITION ===\n")

pc = Computer("Intel i7", 16, 512)
pc.run_program()

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Address Book
class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.street}, {self.city} {self.zip_code}"

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Person HAS-A Address

    def display(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")

address = Address("123 Main St", "Springfield", "12345")
person = Person("Alice", address)
person.display()

# Example 2: University system
class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"{self.code}: {self.name}"

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []  # Student HAS-MANY Courses

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

    def show_courses(self):
        print(f"\n{self.name}'s courses:")
        for course in self.courses:
            print(f"  - {course}")

print("\nUniversity System:")
student = Student("Bob", "S001")
student.enroll(Course("Python Programming", "CS101"))
student.enroll(Course("Data Structures", "CS102"))
student.enroll(Course("Algorithms", "CS103"))
student.show_courses()

# Example 3: Company hierarchy
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} ({self.role})"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"\n{self.name} Department:")
        for emp in self.employees:
            print(f"  - {emp}")

class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def show_structure(self):
        print(f"\n{self.name} Company Structure:")
        for dept in self.departments:
            dept.show_employees()

print("\nCompany Structure:")
company = Company("TechCorp")

# Create departments
engineering = Department("Engineering")
engineering.add_employee(Employee("Alice", "Developer"))
engineering.add_employee(Employee("Bob", "DevOps"))

sales = Department("Sales")
sales.add_employee(Employee("Charlie", "Sales Rep"))
sales.add_employee(Employee("Diana", "Account Manager"))

company.add_department(engineering)
company.add_department(sales)
company.show_structure()

# Example 4: Game character
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None
        self.armor = None

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped {weapon.name}")

    def equip_armor(self, armor):
        self.armor = armor
        print(f"{self.name} equipped {armor.name}")

    def display_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"  Health: {self.health}")
        if self.weapon:
            print(f"  Weapon: {self.weapon.name} (Damage: {self.weapon.damage})")
        if self.armor:
            print(f"  Armor: {self.armor.name} (Defense: {self.armor.defense})")

print("\nGame Character:")
hero = Character("Hero")
hero.equip_weapon(Weapon("Sword", 50))
hero.equip_armor(Armor("Steel Armor", 30))
hero.display_stats()

# Benefits of composition
print("\n=== BENEFITS OF COMPOSITION ===\n")
print("1. Flexibility: Easy to change composed objects")
print("2. Reusability: Components can be used in multiple classes")
print("3. Testability: Test components independently")
print("4. Loose coupling: Classes are less dependent")
print("5. Runtime flexibility: Can change components at runtime")

print("\nComposition over Inheritance:")
print("  - Prefer 'has-a' over 'is-a' when possible")
print("  - More flexible and maintainable")
print("  - Easier to understand and test")
