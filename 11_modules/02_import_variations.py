"""
Import Variations

Python offers several ways to import modules and their components:
- from ... import ... (import specific items)
- import ... as ... (alias)
- from ... import * (import all)

Source: Modules and Packages.docx - Import Variations
"""

# Import specific items
from math import pi, sqrt, ceil, floor

print("=== FROM ... IMPORT ===\n")
print(f"Pi: {pi}")
print(f"Square root of 25: {sqrt(25)}")
print(f"Ceiling of 4.2: {ceil(4.2)}")
print(f"Floor of 4.8: {floor(4.8)}")

# Import with alias
import datetime as dt
import random as rnd

print("\n=== IMPORT AS (ALIAS) ===\n")
today = dt.date.today()
print(f"Today: {today}")
print(f"Random number: {rnd.randint(1, 10)}")

# Import specific item with alias
from math import factorial as fact

print("\n=== FROM ... IMPORT ... AS ===\n")
print(f"Factorial of 5: {fact(5)}")

# Import all (use with caution)
print("\n=== FROM ... IMPORT * ===\n")
print("Note: This imports everything from a module")
print("Not recommended - can cause name conflicts")

# Example with specific imports
from random import choice, shuffle, randint

fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]

print(f"\nRandom fruit: {choice(fruits)}")
print(f"Random number (1-10): {randint(1, 10)}")
shuffle(numbers)
print(f"Shuffled numbers: {numbers}")

# Multiple imports from same module
from datetime import date, time, datetime, timedelta

print("\n=== MULTIPLE FROM SAME MODULE ===\n")
today = date.today()
now = datetime.now()
future = today + timedelta(days=7)

print(f"Today: {today}")
print(f"Now: {now}")
print(f"In 7 days: {future}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Math utilities
from math import pow, log, exp

def compound_interest(principal, rate, time):
    return principal * pow((1 + rate), time)

amount = compound_interest(1000, 0.05, 5)
print(f"Compound interest: ${amount:.2f}")

# Example 2: String utilities
from string import ascii_letters, digits, punctuation

def is_strong_password(password):
    has_letter = any(c in ascii_letters for c in password)
    has_digit = any(c in digits for c in password)
    has_special = any(c in punctuation for c in password)

    return len(password) >= 8 and has_letter and has_digit and has_special

passwords = ["weak", "Strong123!", "NoNumbers!", "short1!"]
print("\nPassword strength:")
for pwd in passwords:
    strength = "Strong" if is_strong_password(pwd) else "Weak"
    print(f"  '{pwd}': {strength}")

# Example 3: Random sampling
from random import sample, choices

population = list(range(1, 51))
lottery_numbers = sample(population, 6)  # 6 unique numbers
print(f"\nLottery numbers: {sorted(lottery_numbers)}")

# Example 4: Date calculations
from datetime import datetime, timedelta

meeting_time = datetime(2024, 12, 31, 14, 30)
reminder_time = meeting_time - timedelta(hours=1)

print(f"\nMeeting: {meeting_time}")
print(f"Reminder: {reminder_time}")

# Import guidelines
print("\n=== IMPORT GUIDELINES ===\n")
print("Preferred:")
print("  import module")
print("  from module import specific_item")
print("  import module as alias (for long names)")
print("\nAvoid:")
print("  from module import * (causes namespace pollution)")
print("\nBest practices:")
print("  - Import at the top of file")
print("  - Group imports: stdlib, third-party, local")
print("  - Use meaningful aliases")
print("  - Import only what you need")

# Common aliases
print("\n=== COMMON ALIASES ===\n")
print("import numpy as np")
print("import pandas as pd")
print("import matplotlib.pyplot as plt")
print("import datetime as dt")
print("import tensorflow as tf")
