"""
List Methods

Lists have many built-in methods for modification:
- append(): Add item to end
- insert(): Add item at specific position
- remove(): Remove specific item
- pop(): Remove and return item
- sort(): Sort the list
- reverse(): Reverse the list
- clear(): Empty the list

Source: 00_review_and_more.docx - Section 7: Lists - Modifying Lists
"""

# ===== APPEND - Add to end =====
print("=== APPEND ===\n")

fruits = ["apple", "banana"]
print(f"Original: {fruits}")

fruits.append("cherry")
print(f"After append('cherry'): {fruits}")

fruits.append("orange")
print(f"After append('orange'): {fruits}")

# ===== INSERT - Add at position =====
print("\n=== INSERT ===\n")

colors = ["red", "blue", "green"]
print(f"Original: {colors}")

colors.insert(1, "yellow")  # Insert at index 1
print(f"After insert(1, 'yellow'): {colors}")

colors.insert(0, "purple")  # Insert at beginning
print(f"After insert(0, 'purple'): {colors}")

# ===== EXTEND - Add multiple items =====
print("\n=== EXTEND ===\n")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"list1: {list1}")
print(f"list2: {list2}")

list1.extend(list2)
print(f"After list1.extend(list2): {list1}")

# Alternative: using + operator
list3 = [7, 8]
result = list1 + list3
print(f"Using + operator: {result}")

# ===== REMOVE - Remove specific item =====
print("\n=== REMOVE ===\n")

fruits = ["apple", "banana", "cherry", "banana"]
print(f"Original: {fruits}")

fruits.remove("banana")  # Removes first occurrence
print(f"After remove('banana'): {fruits}")

# ===== POP - Remove and return item =====
print("\n=== POP ===\n")

numbers = [10, 20, 30, 40, 50]
print(f"Original: {numbers}")

# Pop last item
last = numbers.pop()
print(f"Popped item: {last}")
print(f"After pop(): {numbers}")

# Pop specific index
item = numbers.pop(1)  # Remove and return item at index 1
print(f"Popped item at index 1: {item}")
print(f"After pop(1): {numbers}")

# ===== DEL - Delete by index or slice =====
print("\n=== DEL ===\n")

items = ["a", "b", "c", "d", "e"]
print(f"Original: {items}")

del items[0]  # Delete first item
print(f"After del items[0]: {items}")

del items[1:3]  # Delete slice
print(f"After del items[1:3]: {items}")

# ===== CLEAR - Empty the list =====
print("\n=== CLEAR ===\n")

temp = [1, 2, 3, 4, 5]
print(f"Original: {temp}")

temp.clear()
print(f"After clear(): {temp}")

# ===== SORT - Sort the list =====
print("\n=== SORT ===\n")

numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"Original: {numbers}")

numbers.sort()  # Sort in place (ascending)
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)  # Sort descending
print(f"After sort(reverse=True): {numbers}")

# Sorting strings
words = ["banana", "apple", "cherry"]
print(f"\nWords original: {words}")
words.sort()
print(f"After sort(): {words}")

# ===== REVERSE - Reverse the list =====
print("\n=== REVERSE ===\n")

items = [1, 2, 3, 4, 5]
print(f"Original: {items}")

items.reverse()
print(f"After reverse(): {items}")

# ===== COUNT - Count occurrences =====
print("\n=== COUNT ===\n")

numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"Numbers: {numbers}")

count = numbers.count(2)
print(f"Count of 2: {count}")

count = numbers.count(10)
print(f"Count of 10: {count}")

# ===== INDEX - Find first occurrence =====
print("\n=== INDEX ===\n")

fruits = ["apple", "banana", "cherry", "banana"]
print(f"Fruits: {fruits}")

index = fruits.index("banana")
print(f"Index of 'banana': {index}")

# index with start position
index = fruits.index("banana", 2)  # Search from index 2
print(f"Index of 'banana' from position 2: {index}")

# ===== COPY - Create a copy =====
print("\n=== COPY ===\n")

original = [1, 2, 3]
copied = original.copy()

print(f"Original: {original}")
print(f"Copied: {copied}")

copied.append(4)
print(f"\nAfter modifying copy:")
print(f"Original: {original}")
print(f"Copied: {copied}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Task management
tasks = []
tasks.append("Buy groceries")
tasks.append("Call mom")
tasks.append("Finish homework")
print("Tasks:", tasks)

# Complete a task
completed = tasks.pop(0)
print(f"Completed: {completed}")
print(f"Remaining tasks: {tasks}")

# Example 2: Sorting scores
scores = [85, 92, 78, 95, 88]
print(f"\nOriginal scores: {scores}")
scores.sort(reverse=True)  # Highest to lowest
print(f"Sorted (high to low): {scores}")
print(f"Highest score: {scores[0]}")
print(f"Lowest score: {scores[-1]}")
