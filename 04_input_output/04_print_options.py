"""
Print Function Options

The print() function has optional parameters:
- sep: separator between multiple items (default: space)
- end: what to print at the end (default: newline)

Source: 00_review_and_more.docx - Section 5: Input and Output - Print options
"""

# Default behavior
print("=== DEFAULT BEHAVIOR ===")
print("apple", "banana", "cherry")  # Default separator is space
print("Line 1")
print("Line 2")  # Default end is newline

# ===== SEP PARAMETER =====
print("\n=== SEP PARAMETER ===")

# Custom separator
print("apple", "banana", "cherry", sep=", ")

# Using different separators
print("2025", "01", "15", sep="-")  # Date format

# Using | as separator
print("Name", "Age", "City", sep=" | ")

# Using newline as separator
print("First", "Second", "Third", sep="\n")

# No separator (empty string)
print("one", "two", "three", sep="")

# Multiple characters as separator
print("Python", "Java", "C++", sep=" <-> ")

# ===== END PARAMETER =====
print("\n=== END PARAMETER ===")

# Print on same line
print("Hello", end=" ")
print("World")  # Prints "Hello World" on same line

# Custom end character
print("Loading", end="...")
print("Done!")

# No newline at end
print("Enter your choice: ", end="")
print("[Y/N]")

# Multiple prints on same line
print("Progress: ", end="")
print("[", end="")
print("=====>", end="")
print("]", end=" ")
print("50%")

# ===== COMBINING SEP AND END =====
print("\n=== COMBINING SEP AND END ===")

# Both sep and end together
print("apple", "banana", "cherry", sep=", ", end=".\n")

# Creating a progress bar
print("Loading: ", end="")
for i in range(5):
    print("█", end="", sep="")
print(" Complete!")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: CSV format
print("\nCSV Format:")
print("Name", "Age", "City", sep=",")
print("Alice", "25", "New York", sep=",")
print("Bob", "30", "Los Angeles", sep=",")

# Example 2: Menu display
print("\nMenu:")
print("1", "Start Game", sep=". ")
print("2", "Load Game", sep=". ")
print("3", "Settings", sep=". ")
print("4", "Exit", sep=". ")

# Example 3: Countdown
print("\nCountdown:")
for i in range(5, 0, -1):
    print(i, end="... ")
print("Go!")

# Example 4: Path formatting
print("\nFile Path:")
print("C:", "Users", "Documents", "file.txt", sep="\\")

# Example 5: List formatting
print("\nIngredients:")
items = ["Flour", "Sugar", "Eggs", "Butter"]
for i, item in enumerate(items, 1):
    print(f"{i}", item, sep=". ", end="\n")

# Example 6: Same line output
print("\nProcessing", end="")
print(".", end="")
print(".", end="")
print(".", end=" ")
print("Complete!")

# Example 7: Table header
print("\n" + "=" * 50)
print("ID", "Name", "Score", sep=" | ")
print("=" * 50)
print("001", "Alice", "95", sep=" | ")
print("002", "Bob", "87", sep=" | ")
print("003", "Charlie", "92", sep=" | ")
print("=" * 50)
