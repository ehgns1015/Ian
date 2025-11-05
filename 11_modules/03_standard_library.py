"""
Standard Library

Python comes with a rich standard library of modules.
These modules provide functionality for common tasks without installing anything extra.

Source: Modules and Packages.docx - Standard Library
"""

# os module - Operating system interface
import os

print("=== OS MODULE ===\n")
print(f"Current directory: {os.getcwd()}")
print(f"User home directory: {os.path.expanduser('~')}")
print(f"Operating system: {os.name}")

# Path operations
file_path = os.path.join("folder", "subfolder", "file.txt")
print(f"Joined path: {file_path}")

# sys module - System-specific parameters
import sys

print("\n=== SYS MODULE ===\n")
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Max integer: {sys.maxsize}")

# json module - JSON encoding/decoding
import json

print("\n=== JSON MODULE ===\n")

# Python to JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "gaming"]
}

json_string = json.dumps(data, indent=2)
print("Python to JSON:")
print(json_string)

# JSON to Python
json_data = '{"product": "Laptop", "price": 999.99, "in_stock": true}'
parsed = json.loads(json_data)
print(f"\nJSON to Python: {parsed}")
print(f"Product: {parsed['product']}, Price: ${parsed['price']}")

# collections module - Specialized containers
from collections import Counter, defaultdict, namedtuple

print("\n=== COLLECTIONS MODULE ===\n")

# Counter - Count occurrences
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_count = Counter(words)
print(f"Word count: {word_count}")
print(f"Most common: {word_count.most_common(2)}")

# defaultdict - Dictionary with default values
scores = defaultdict(int)  # Default value is 0
scores['Alice'] += 10
scores['Bob'] += 5
scores['Alice'] += 15
print(f"\nScores: {dict(scores)}")

# namedtuple - Tuple with named fields
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"\nPoint: ({p.x}, {p.y})")

# re module - Regular expressions
import re

print("\n=== RE MODULE (REGEX) ===\n")

text = "Contact us at support@example.com or sales@example.com"
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print(f"Found emails: {emails}")

# Pattern matching
phone = "Phone: 555-1234"
match = re.search(r'\d{3}-\d{4}', phone)
if match:
    print(f"Found phone: {match.group()}")

# time module - Time-related functions
import time

print("\n=== TIME MODULE ===\n")

print("Sleeping for 1 second...")
start = time.time()
time.sleep(1)
end = time.time()
print(f"Elapsed: {end - start:.2f} seconds")

# Timestamp
timestamp = time.time()
print(f"Unix timestamp: {timestamp}")

# pathlib module - Object-oriented file paths
from pathlib import Path

print("\n=== PATHLIB MODULE ===\n")

current_file = Path(__file__)
print(f"Current file: {current_file.name}")
print(f"Parent directory: {current_file.parent.name}")
print(f"File extension: {current_file.suffix}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: File size formatter
def format_bytes(bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0

print("File sizes:")
print(format_bytes(1024))
print(format_bytes(1048576))
print(format_bytes(1073741824))

# Example 2: Word frequency analyzer
from collections import Counter

def analyze_text(text):
    words = text.lower().split()
    word_freq = Counter(words)
    return word_freq

text = "python is great python is powerful python is easy"
freq = analyze_text(text)
print(f"\nWord frequency: {freq}")

# Example 3: Data validation with regex
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

emails = ["valid@example.com", "invalid.email", "test@test.co.uk"]
print("\nEmail validation:")
for email in emails:
    valid = "Valid" if validate_email(email) else "Invalid"
    print(f"  {email}: {valid}")

# Example 4: JSON configuration
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "logging": {
        "level": "INFO",
        "file": "app.log"
    }
}

# Save to string (in real app, save to file)
config_json = json.dumps(config, indent=2)
print("\nConfiguration:")
print(config_json)

# Standard library highlights
print("\n=== USEFUL STANDARD LIBRARY MODULES ===\n")
print("File & Path: os, pathlib, shutil, glob")
print("Data: json, csv, sqlite3, pickle")
print("Text: re, string, textwrap")
print("Date/Time: datetime, time, calendar")
print("Math: math, statistics, decimal, fractions")
print("Collections: collections, heapq, bisect")
print("Functional: itertools, functools")
print("System: sys, os, subprocess, argparse")
print("Internet: urllib, http, email, html")
print("Testing: unittest, doctest")
