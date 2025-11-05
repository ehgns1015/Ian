"""
Sets

Sets are unordered, mutable collections of unique elements.
Sets automatically remove duplicates and are useful for mathematical operations.
Sets are created using curly braces {} or set().

Source: 00_review_and_more.docx - Section 10: Sets
"""

# ===== CREATING SETS =====
print("=== CREATING SETS ===\n")

# Empty set (must use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with items
fruits = {"apple", "banana", "cherry"}
print(f"Fruits: {fruits}")

# Set automatically removes duplicates
numbers = {1, 2, 3, 2, 1, 4, 3}
print(f"Numbers (with duplicates): {numbers}")  # Duplicates removed

# Creating set from list
list_data = [1, 2, 2, 3, 3, 3, 4]
set_data = set(list_data)
print(f"List: {list_data}")
print(f"Set: {set_data}")

# Creating set from string (unique characters)
char_set = set("hello")
print(f"Set from 'hello': {char_set}")

# ===== ADDING ELEMENTS =====
print("\n=== ADDING ELEMENTS ===\n")

fruits = {"apple", "banana"}
print(f"Original: {fruits}")

# Add single element
fruits.add("cherry")
print(f"After add('cherry'): {fruits}")

# Adding duplicate (no effect)
fruits.add("apple")
print(f"After add('apple') again: {fruits}")

# Update with multiple elements
fruits.update(["orange", "mango", "kiwi"])
print(f"After update with list: {fruits}")

# ===== REMOVING ELEMENTS =====
print("\n=== REMOVING ELEMENTS ===\n")

colors = {"red", "blue", "green", "yellow"}
print(f"Original: {colors}")

# remove() - Removes element (raises error if not found)
colors.remove("blue")
print(f"After remove('blue'): {colors}")

# discard() - Removes element (no error if not found)
colors.discard("purple")  # No error
print(f"After discard('purple'): {colors}")

# pop() - Remove and return arbitrary element
removed = colors.pop()
print(f"Popped element: {removed}")
print(f"After pop(): {colors}")

# clear() - Remove all elements
temp = {1, 2, 3}
temp.clear()
print(f"After clear(): {temp}")

# ===== SET OPERATIONS =====
print("\n=== SET OPERATIONS ===\n")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union (all elements from both sets)
union = set1 | set2
print(f"\nUnion (set1 | set2): {union}")

# Alternative: union() method
union_method = set1.union(set2)
print(f"Union (set1.union(set2)): {union_method}")

# Intersection (common elements)
intersection = set1 & set2
print(f"\nIntersection (set1 & set2): {intersection}")

# Alternative: intersection() method
intersection_method = set1.intersection(set2)
print(f"Intersection (set1.intersection(set2)): {intersection_method}")

# Difference (elements in set1 but not in set2)
difference = set1 - set2
print(f"\nDifference (set1 - set2): {difference}")

# Alternative: difference() method
difference_method = set1.difference(set2)
print(f"Difference (set1.difference(set2)): {difference_method}")

# Symmetric difference (elements in either set, but not both)
symmetric_diff = set1 ^ set2
print(f"\nSymmetric diff (set1 ^ set2): {symmetric_diff}")

# ===== MEMBERSHIP =====
print("\n=== MEMBERSHIP ===\n")

fruits = {"apple", "banana", "cherry"}

if "apple" in fruits:
    print("Apple is in the set")

if "orange" not in fruits:
    print("Orange is not in the set")

# ===== SET SIZE =====
print("\n=== SIZE ===\n")

numbers = {1, 2, 3, 4, 5}
print(f"Set: {numbers}")
print(f"Size: {len(numbers)}")

# ===== SUBSET AND SUPERSET =====
print("\n=== SUBSET AND SUPERSET ===\n")

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Check if subset
is_subset = set_a.issubset(set_b)
print(f"A is subset of B: {is_subset}")

# Check if superset
is_superset = set_b.issuperset(set_a)
print(f"B is superset of A: {is_superset}")

# Check if disjoint (no common elements)
set_c = {6, 7, 8}
is_disjoint = set_a.isdisjoint(set_c)
print(f"A and C are disjoint: {is_disjoint}")

# ===== FROZEN SETS (Immutable) =====
print("\n=== FROZEN SETS ===\n")

# Frozen set cannot be modified
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen}")

# Frozen sets can be used as dictionary keys
dict_with_set_key = {frozen: "value"}
print(f"Dict with frozen set key: {dict_with_set_key}")

# ===== ITERATING =====
print("\n=== ITERATING ===\n")

colors = {"red", "blue", "green"}
print("Colors:")
for color in colors:
    print(f"  - {color}")

# ===== SET COMPREHENSION =====
print("\n=== SET COMPREHENSION ===\n")

# Create set of squares
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Filter even numbers
evens = {x for x in range(1, 11) if x % 2 == 0}
print(f"Even numbers: {evens}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Remove duplicates from list
numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = list(set(numbers_list))
print(f"Original list: {numbers_list}")
print(f"Unique values: {unique_numbers}")

# Example 2: Find common interests
alice_interests = {"reading", "hiking", "cooking", "gaming"}
bob_interests = {"gaming", "cooking", "photography", "traveling"}

common = alice_interests & bob_interests
print(f"\nAlice's interests: {alice_interests}")
print(f"Bob's interests: {bob_interests}")
print(f"Common interests: {common}")

# Example 3: Find unique visitors
day1_visitors = {"Alice", "Bob", "Charlie", "David"}
day2_visitors = {"Bob", "David", "Eve", "Frank"}

all_visitors = day1_visitors | day2_visitors
return_visitors = day1_visitors & day2_visitors
new_visitors = day2_visitors - day1_visitors

print(f"\nDay 1 visitors: {day1_visitors}")
print(f"Day 2 visitors: {day2_visitors}")
print(f"All unique visitors: {all_visitors}")
print(f"Return visitors: {return_visitors}")
print(f"New visitors on day 2: {new_visitors}")

# Example 4: Check permissions
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_all_permissions = required_permissions.issubset(user_permissions)
missing_permissions = required_permissions - user_permissions

print(f"\nRequired: {required_permissions}")
print(f"User has: {user_permissions}")
print(f"Has all permissions: {has_all_permissions}")
print(f"Missing: {missing_permissions}")

# Example 5: Find unique words
text = "hello world hello python world"
unique_words = set(text.split())
print(f"\nText: '{text}'")
print(f"Unique words: {unique_words}")
print(f"Number of unique words: {len(unique_words)}")
