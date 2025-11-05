"""
Special Methods (Magic Methods)

Special methods (also called dunder methods) have double underscores.
They allow you to define how objects behave with built-in operations.

Common special methods:
- __init__: Constructor
- __str__: String representation
- __repr__: Official string representation
- __len__: Length
- __add__, __sub__, etc.: Operator overloading

Source: Object.docx - Section 6: Special Methods
"""

# __str__ method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

print("=== __str__ METHOD ===\n")

book = Book("1984", "George Orwell")
print(book)  # Calls __str__ method

# __repr__ method
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point at ({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

print("\n=== __repr__ METHOD ===\n")

p = Point(3, 4)
print(str(p))  # Calls __str__
print(repr(p))  # Calls __repr__
print(p)  # Uses __str__ if available, else __repr__

# __len__ method
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"Playlist '{self.name}' with {len(self)} songs"

print("\n=== __len__ METHOD ===\n")

playlist = Playlist("My Favorites")
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")

print(playlist)
print(f"Length: {len(playlist)}")  # Calls __len__

# Comparison methods
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):  # ==
        return self.grade == other.grade

    def __lt__(self, other):  # <
        return self.grade < other.grade

    def __le__(self, other):  # <=
        return self.grade <= other.grade

    def __str__(self):
        return f"{self.name} (Grade: {self.grade})"

print("\n=== COMPARISON METHODS ===\n")

student1 = Student("Alice", 85)
student2 = Student("Bob", 90)
student3 = Student("Charlie", 85)

print(f"{student1} == {student3}: {student1 == student3}")
print(f"{student1} < {student2}: {student1 < student2}")
print(f"{student2} <= {student1}: {student2 <= student1}")

# Arithmetic operators
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __mul__(self, factor):
        return Money(self.amount * factor)

    def __str__(self):
        return f"${self.amount:.2f}"

print("\n=== ARITHMETIC OPERATORS ===\n")

money1 = Money(100)
money2 = Money(50)

print(f"{money1} + {money2} = {money1 + money2}")
print(f"{money1} - {money2} = {money1 - money2}")
print(f"{money1} * 2 = {money1 * 2}")

# Container methods
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

print("\n=== CONTAINER METHODS ===\n")

cart = ShoppingCart()
cart.add("Apple")
cart.add("Banana")
cart.add("Cherry")

print(f"Cart length: {len(cart)}")
print(f"First item: {cart[0]}")
print(f"'Banana' in cart: {'Banana' in cart}")

print("Items:")
for item in cart:
    print(f"  - {item}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Temperature class
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __add__(self, other):
        return Temperature(self.celsius + other.celsius)

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

temp1 = Temperature(20)
temp2 = Temperature(25)
temp3 = Temperature(20)

print(f"Temperature 1: {temp1}")
print(f"Temperature 2: {temp2}")
print(f"{temp1} < {temp2}: {temp1 < temp2}")
print(f"{temp1} == {temp3}: {temp1 == temp3}")
print(f"{temp1} + {temp2} = {temp1 + temp2}")

# Example 2: Vector class
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

print("\nVector Operations:")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 * 3: {v1 * 3}")
print(f"Length of v1: {len(v1)}")

# Common special methods
print("\n=== COMMON SPECIAL METHODS ===\n")
print("Object creation/deletion:")
print("  __init__: Constructor")
print("  __del__: Destructor")

print("\nString representation:")
print("  __str__: User-friendly string")
print("  __repr__: Developer-friendly string")

print("\nComparison:")
print("  __eq__, __ne__, __lt__, __le__, __gt__, __ge__")

print("\nArithmetic:")
print("  __add__, __sub__, __mul__, __truediv__, __floordiv__")

print("\nContainer:")
print("  __len__, __getitem__, __setitem__, __contains__")
print("  __iter__, __next__")

print("\nOther:")
print("  __call__: Make object callable")
print("  __bool__: Truth value testing")
