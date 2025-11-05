"""
Finally Clause

The finally block always executes, whether an exception occurred or not.
Commonly used for cleanup operations (closing files, releasing resources).

Source: Error Handling.docx - Finally Clause
"""

# Basic try-except-finally
print("=== BASIC FINALLY ===\n")

try:
    print("Trying operation...")
    result = 10 / 2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error occurred")
finally:
    print("Finally block always executes")

# Finally with exception
print("\n=== FINALLY WITH EXCEPTION ===\n")

try:
    print("Trying risky operation...")
    result = 10 / 0
except ZeroDivisionError:
    print("Caught division by zero")
finally:
    print("Cleanup performed")

# Finally without exception
print("\n=== FINALLY WITHOUT EXCEPTION ===\n")

try:
    print("Trying safe operation...")
    result = 10 + 20
    print(f"Result: {result}")
finally:
    print("Finally executes even without errors")

# Try-finally without except
print("\n=== TRY-FINALLY (NO EXCEPT) ===\n")

def open_file_demo():
    try:
        print("Opening file...")
        # file operation would go here
    finally:
        print("Closing file (cleanup)")

open_file_demo()

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: File handling
print("=== FILE HANDLING ===")

def read_file_with_finally(filename):
    file = None
    try:
        print(f"Opening {filename}...")
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    finally:
        if file:
            file.close()
            print("File closed")

read_file_with_finally("test.txt")

# Example 2: Resource management
print("\n=== RESOURCE MANAGEMENT ===")

class DatabaseConnection:
    def __init__(self, name):
        self.name = name
        self.connected = False

    def connect(self):
        print(f"Connecting to {self.name}...")
        self.connected = True

    def disconnect(self):
        print(f"Disconnecting from {self.name}...")
        self.connected = False

def query_database(connection):
    try:
        connection.connect()
        print("Executing query...")
        # Simulate query
        result = 100 / 10  # Could be 100 / 0 for error
        print(f"Query result: {result}")
        return result
    except ZeroDivisionError:
        print("Query failed")
        return None
    finally:
        connection.disconnect()

db = DatabaseConnection("TestDB")
query_database(db)

# Example 3: Counter with finally
print("\n=== COUNTER WITH FINALLY ===")

attempts = 0

def process_with_counter(value):
    global attempts
    try:
        attempts += 1
        print(f"Attempt #{attempts}")
        result = 100 / value
        print(f"Success: {result}")
        return result
    except ZeroDivisionError:
        print("Failed: Division by zero")
        return None
    finally:
        print(f"Total attempts so far: {attempts}\n")

process_with_counter(10)
process_with_counter(0)
process_with_counter(5)

# Example 4: Lock/Unlock pattern
print("=== LOCK/UNLOCK PATTERN ===")

class Resource:
    def __init__(self, name):
        self.name = name
        self.locked = False

    def lock(self):
        print(f"Locking {self.name}")
        self.locked = True

    def unlock(self):
        print(f"Unlocking {self.name}")
        self.locked = False

def use_resource(resource, cause_error=False):
    try:
        resource.lock()
        print("Using resource...")
        if cause_error:
            raise ValueError("Simulated error")
        print("Operation successful")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        resource.unlock()
        print()

res = Resource("SharedResource")
use_resource(res, False)
use_resource(res, True)

# Example 5: Timer
print("=== TIMER PATTERN ===")

import time

def timed_operation(duration, cause_error=False):
    start_time = time.time()
    try:
        print(f"Starting operation...")
        time.sleep(duration / 1000)  # Convert to seconds
        if cause_error:
            raise Exception("Operation failed")
        print("Operation completed")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        elapsed = (time.time() - start_time) * 1000
        print(f"Time elapsed: {elapsed:.2f}ms\n")

timed_operation(100, False)
timed_operation(50, True)

# Important notes
print("=== FINALLY NOTES ===\n")
print("1. Finally ALWAYS executes")
print("2. Executes even if there's a return in try/except")
print("3. Executes even if exception is not caught")
print("4. Perfect for cleanup: close files, release locks, etc.")
print("5. Use 'with' statement for file handling (better practice)")

# With statement (better than try-finally for files)
print("\n=== WITH STATEMENT (RECOMMENDED) ===")
print("Instead of:")
print("  try:")
print("    file = open('file.txt')")
print("  finally:")
print("    file.close()")
print("\nUse:")
print("  with open('file.txt') as file:")
print("    # file automatically closed")
