"""
Creating Your Own Modules

You can create your own modules by saving Python code in .py files.
Any Python file can be imported as a module.

Source: Modules and Packages.docx - Creating Modules
"""

# To demonstrate, we'll create example module content here
# In practice, you would save this in a separate .py file

print("=== CREATING MODULES ===\n")
print("A module is simply a .py file with Python code.\n")

# Example module structure
print("Example: my_math.py")
print("-" * 40)
print("""
# my_math.py

def add(a, b):
    '''Add two numbers'''
    return a + b

def subtract(a, b):
    '''Subtract two numbers'''
    return a - b

def multiply(a, b):
    '''Multiply two numbers'''
    return a * b

PI = 3.14159

class Calculator:
    def __init__(self):
        self.result = 0

    def calculate(self, operation, a, b):
        if operation == '+':
            self.result = add(a, b)
        elif operation == '-':
            self.result = subtract(a, b)
        elif operation == '*':
            self.result = multiply(a, b)
        return self.result
""")

print("\n" + "=" * 40)
print("\nTo use this module:")
print("  import my_math")
print("  result = my_math.add(5, 3)")
print("  print(my_math.PI)")
print("  calc = my_math.Calculator()")

# Module best practices
print("\n=== MODULE BEST PRACTICES ===\n")

print("1. Module naming:")
print("   - Use lowercase with underscores")
print("   - Be descriptive: string_utils.py, not utils.py")
print("   - Avoid built-in names")

print("\n2. Module structure:")
print("   - Imports at top")
print("   - Constants in UPPERCASE")
print("   - Functions and classes")
print("   - if __name__ == '__main__': for testing")

print("\n3. Documentation:")
print("   - Module docstring at top")
print("   - Function docstrings")
print("   - Clear comments")

# Example with __name__ check
print("\n=== __name__ CHECK ===\n")

example_code = '''
# utilities.py

def greet(name):
    """Greet a person"""
    return f"Hello, {name}!"

def main():
    """Test function"""
    print(greet("World"))

if __name__ == "__main__":
    # This runs only when file is executed directly
    main()
else:
    # This runs when file is imported
    print("utilities module loaded")
'''

print(example_code)
print("\nWhen run directly: executes main()")
print("When imported: just loads the module")

# Practical module example
print("\n=== PRACTICAL MODULE EXAMPLE ===\n")

print("Example: string_utils.py")
print("-" * 40)

practical_example = '''
"""
String utility functions for common text operations.
"""

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def capitalize_words(text):
    """Capitalize each word"""
    return ' '.join(word.capitalize() for word in text.split())

def count_vowels(text):
    """Count vowels in text"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def remove_whitespace(text):
    """Remove all whitespace"""
    return ''.join(text.split())

class TextFormatter:
    """Format text in various ways"""

    @staticmethod
    def to_title_case(text):
        return text.title()

    @staticmethod
    def to_snake_case(text):
        return text.lower().replace(' ', '_')

    @staticmethod
    def to_camel_case(text):
        words = text.split()
        return words[0].lower() + ''.join(w.capitalize() for w in words[1:])

# Module-level constant
MAX_LENGTH = 1000

# Example usage
if __name__ == "__main__":
    text = "hello world"
    print(f"Original: {text}")
    print(f"Reversed: {reverse_string(text)}")
    print(f"Capitalized: {capitalize_words(text)}")
    print(f"Vowels: {count_vowels(text)}")
    print(f"No spaces: {remove_whitespace(text)}")

    formatter = TextFormatter()
    print(f"Title: {formatter.to_title_case(text)}")
    print(f"Snake: {formatter.to_snake_case(text)}")
    print(f"Camel: {formatter.to_camel_case(text)}")
'''

print(practical_example)

# Module organization tips
print("\n=== MODULE ORGANIZATION ===\n")

print("Single file module:")
print("  my_module.py")

print("\nPackage (multiple modules):")
print("  my_package/")
print("    __init__.py")
print("    module1.py")
print("    module2.py")

print("\nProject structure:")
print("  project/")
print("    __init__.py")
print("    core/")
print("      __init__.py")
print("      engine.py")
print("    utils/")
print("      __init__.py")
print("      helpers.py")
print("    tests/")
print("      test_engine.py")

# Common module patterns
print("\n=== COMMON MODULE PATTERNS ===\n")

print("1. Utility module:")
print("   - Collection of helper functions")
print("   - Example: string_utils, file_utils")

print("\n2. Configuration module:")
print("   - Store settings and constants")
print("   - Example: config.py, settings.py")

print("\n3. Data module:")
print("   - Define data structures")
print("   - Example: models.py, schemas.py")

print("\n4. API module:")
print("   - Interface for external interaction")
print("   - Example: api.py, endpoints.py")

# Creating reusable code
print("\n=== MAKING CODE REUSABLE ===\n")

print("1. Keep functions small and focused")
print("2. Use clear, descriptive names")
print("3. Add docstrings and type hints")
print("4. Handle errors gracefully")
print("5. Avoid global state")
print("6. Make dependencies explicit")
print("7. Write tests")

print("\nExample with type hints and docstrings:")

type_hint_example = '''
def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate discounted price.

    Args:
        price: Original price
        discount_percent: Discount percentage (0-100)

    Returns:
        Final price after discount

    Raises:
        ValueError: If discount is not between 0 and 100
    """
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    discount = price * (discount_percent / 100)
    return price - discount
'''

print(type_hint_example)
