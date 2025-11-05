"""
Instance Variables vs Class Variables

Instance variables: Unique to each object (self.variable)
Class variables: Shared by all objects of the class

Source: Object.docx - Section 2: Instance vs Class Variables
"""

# Class variable example
class Dog:
    species = "Canine"  # Class variable (shared by all dogs)

    def __init__(self, name):
        self.name = name  # Instance variable (unique to each dog)

print("=== CLASS VS INSTANCE VARIABLES ===\n")

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(f"{dog1.name}: {dog1.species}")
print(f"{dog2.name}: {dog2.species}")

# Modifying class variable
print("\n=== MODIFYING CLASS VARIABLE ===\n")
print(f"Before: {Dog.species}")
Dog.species = "Canis familiaris"
print(f"After: {Dog.species}")
print(f"dog1 sees: {dog1.species}")
print(f"dog2 sees: {dog2.species}")

# Instance variable modification
print("\n=== MODIFYING INSTANCE VARIABLE ===\n")
dog1.name = "Buddy Jr."
print(f"dog1 name: {dog1.name}")
print(f"dog2 name: {dog2.name}")  # Unchanged

# Class variable for counting instances
class Employee:
    company = "TechCorp"  # Class variable
    employee_count = 0  # Class variable for counting

    def __init__(self, name, role):
        self.name = name  # Instance variable
        self.role = role  # Instance variable
        Employee.employee_count += 1  # Increment class variable

print("\n=== COUNTING INSTANCES ===\n")

print(f"Initial count: {Employee.employee_count}")

emp1 = Employee("Alice", "Developer")
print(f"After creating emp1: {Employee.employee_count}")

emp2 = Employee("Bob", "Designer")
print(f"After creating emp2: {Employee.employee_count}")

emp3 = Employee("Charlie", "Manager")
print(f"After creating emp3: {Employee.employee_count}")

# Accessing class variables
print("\n=== ACCESSING CLASS VARIABLES ===\n")
print(f"Via class: {Employee.company}")
print(f"Via instance: {emp1.company}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Bank with interest rate
class BankAccount:
    interest_rate = 0.03  # Class variable (same for all accounts)

    def __init__(self, owner, balance):
        self.owner = owner  # Instance variable
        self.balance = balance  # Instance variable

    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

print("Bank Accounts:")
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)

print(f"{acc1.owner}: ${acc1.balance}")
print(f"{acc2.owner}: ${acc2.balance}")

# Change interest rate for all accounts
BankAccount.interest_rate = 0.05

acc1.apply_interest()
acc2.apply_interest()

print(f"\nAfter interest ({BankAccount.interest_rate * 100}%):")
print(f"{acc1.owner}: ${acc1.balance:.2f}")
print(f"{acc2.owner}: ${acc2.balance:.2f}")

# Example 2: Product with category
class Product:
    category = "General"  # Class variable
    all_products = []  # Class variable (list)

    def __init__(self, name, price):
        self.name = name  # Instance variable
        self.price = price  # Instance variable
        Product.all_products.append(self)

Product.category = "Electronics"

laptop = Product("Laptop", 999.99)
mouse = Product("Mouse", 29.99)

print(f"\nCategory: {Product.category}")
print(f"Total products: {len(Product.all_products)}")
for prod in Product.all_products:
    print(f"  - {prod.name}: ${prod.price}")

# Example 3: Counter with ID generation
class User:
    next_id = 1  # Class variable for auto-incrementing ID

    def __init__(self, username):
        self.user_id = User.next_id  # Instance variable
        self.username = username  # Instance variable
        User.next_id += 1

print("\nUser IDs:")
user1 = User("alice")
user2 = User("bob")
user3 = User("charlie")

print(f"User: {user1.username}, ID: {user1.user_id}")
print(f"User: {user2.username}, ID: {user2.user_id}")
print(f"User: {user3.username}, ID: {user3.user_id}")
print(f"Next ID will be: {User.next_id}")

# Key differences
print("\n=== KEY DIFFERENCES ===\n")
print("Instance Variables:")
print("  - Defined in __init__ with self")
print("  - Unique to each object")
print("  - Accessed via self.variable")
print("  - Different for each instance")

print("\nClass Variables:")
print("  - Defined in class body")
print("  - Shared by all objects")
print("  - Accessed via ClassName.variable")
print("  - Same for all instances")
print("  - Can be modified to affect all instances")
