"""
Packages

Packages are directories containing multiple modules.
They allow you to organize related modules together.
A package must contain an __init__.py file (can be empty).

Source: Modules and Packages.docx - Packages
"""

print("=== WHAT IS A PACKAGE? ===\n")

print("A package is a directory with:")
print("  1. __init__.py file (required)")
print("  2. One or more Python modules (.py files)")
print("  3. Optionally, sub-packages (nested directories)")

# Package structure example
print("\n=== BASIC PACKAGE STRUCTURE ===\n")

structure = """
my_package/
    __init__.py         # Makes this directory a package
    module1.py          # First module
    module2.py          # Second module
    subpackage/
        __init__.py     # Sub-package
        module3.py      # Module in sub-package
"""

print(structure)

# Importing from packages
print("=== IMPORTING FROM PACKAGES ===\n")

print("Import entire module:")
print("  import my_package.module1")
print("  my_package.module1.function()")

print("\nImport specific function:")
print("  from my_package.module1 import function")
print("  function()")

print("\nImport from sub-package:")
print("  from my_package.subpackage import module3")
print("  module3.function()")

# __init__.py file
print("\n=== __init__.py FILE ===\n")

print("The __init__.py file:")
print("  - Makes directory a Python package")
print("  - Can be empty")
print("  - Can initialize package")
print("  - Can expose package API")

print("\nExample __init__.py:")

init_example = """
# my_package/__init__.py

# Import commonly used items
from .module1 import function1
from .module2 import Class2

# Package metadata
__version__ = '1.0.0'
__author__ = 'Your Name'

# Initialize package
print(f"Loading {__name__} version {__version__}")

# Define what 'from package import *' imports
__all__ = ['function1', 'Class2']
"""

print(init_example)

# Real-world package example
print("\n=== PRACTICAL PACKAGE EXAMPLE ===\n")

print("Example: math_tools package")
print("-" * 50)

practical = """
math_tools/
    __init__.py
    basic.py
    advanced.py
    constants.py

# __init__.py
from .basic import add, subtract
from .constants import PI, E
__version__ = '1.0.0'
__all__ = ['add', 'subtract', 'PI', 'E']

# basic.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# advanced.py
import math

def factorial(n):
    return math.factorial(n)

def power(base, exp):
    return base ** exp

# constants.py
PI = 3.14159265359
E = 2.71828182846

# Usage:
import math_tools
print(math_tools.add(5, 3))
print(math_tools.PI)

from math_tools.advanced import factorial
print(factorial(5))
"""

print(practical)

# Sub-packages
print("\n=== SUB-PACKAGES ===\n")

subpackage_structure = """
game/
    __init__.py
    engine/
        __init__.py
        graphics.py
        physics.py
    ai/
        __init__.py
        pathfinding.py
        decision.py
    utils/
        __init__.py
        helpers.py
        math.py

# Importing:
from game.engine import graphics
from game.ai.pathfinding import find_path
import game.utils.math
"""

print(subpackage_structure)

# Relative imports
print("\n=== RELATIVE IMPORTS ===\n")

print("Absolute import:")
print("  from game.engine import graphics")

print("\nRelative import (within package):")
print("  from . import graphics          # Current directory")
print("  from .. import utils             # Parent directory")
print("  from ..ai import pathfinding     # Sibling directory")

relative_example = """
# In game/engine/physics.py

from . import graphics              # Import graphics from same directory
from ..ai import decision           # Import from sibling package
from ..utils.math import Vector2D   # Import from another sibling
"""

print("\nExample:")
print(relative_example)

# Package organization patterns
print("\n=== PACKAGE ORGANIZATION PATTERNS ===\n")

print("1. Flat Package:")
flat = """
mylib/
    __init__.py
    utils.py
    helpers.py
    core.py
"""
print(flat)

print("\n2. Feature-based:")
feature = """
webapp/
    __init__.py
    users/
        __init__.py
        models.py
        views.py
    products/
        __init__.py
        models.py
        views.py
    orders/
        __init__.py
        models.py
        views.py
"""
print(feature)

print("\n3. Layer-based:")
layer = """
application/
    __init__.py
    models/
        __init__.py
        user.py
        product.py
    views/
        __init__.py
        user_views.py
        product_views.py
    controllers/
        __init__.py
        user_controller.py
"""
print(layer)

# Best practices
print("\n=== PACKAGE BEST PRACTICES ===\n")

print("1. Clear structure:")
print("   - Group related functionality")
print("   - Keep packages focused")
print("   - Use meaningful names")

print("\n2. __init__.py usage:")
print("   - Import commonly used items")
print("   - Set __version__ and __author__")
print("   - Define __all__ for public API")

print("\n3. Documentation:")
print("   - README.md in package root")
print("   - Docstrings in __init__.py")
print("   - Examples and usage guide")

print("\n4. Testing:")
print("   - tests/ directory")
print("   - Test each module")
print("   - Use pytest or unittest")

# Example project structure
print("\n=== COMPLETE PROJECT STRUCTURE ===\n")

complete = """
my_project/
    README.md
    setup.py
    requirements.txt
    my_package/
        __init__.py
        core/
            __init__.py
            engine.py
        utils/
            __init__.py
            helpers.py
        tests/
            __init__.py
            test_engine.py
            test_helpers.py
    docs/
        conf.py
        index.rst
    examples/
        basic_usage.py
"""

print(complete)

# Namespace packages
print("\n=== ADVANCED: NAMESPACE PACKAGES ===\n")

print("Namespace packages (PEP 420):")
print("  - No __init__.py required (Python 3.3+)")
print("  - Split across multiple directories")
print("  - Used for large projects")

print("\nExample:")
namespace = """
project1/
    company/
        product_a/
            module1.py

project2/
    company/
        product_b/
            module2.py

# Both can be imported as:
from company.product_a import module1
from company.product_b import module2
"""
print(namespace)
