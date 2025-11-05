"""
Type Conversion (Type Casting)

Python allows you to convert between different data types.
This is called type conversion or type casting.

Source: 00_review_and_more.docx - Section 3: Type Conversion
"""

# Converting to integer
print("=== Converting to Integer ===")

# Float to int (truncates decimal part)
float_num = 10.8
int_from_float = int(float_num)
print(f"int(10.8) = {int_from_float}")

# String to int
str_num = "100"
int_from_string = int(str_num)
print(f"int('100') = {int_from_string}")

# Boolean to int
bool_value = True
int_from_bool = int(bool_value)  # True = 1, False = 0
print(f"int(True) = {int_from_bool}")

# Converting to float
print("\n=== Converting to Float ===")

# Int to float
integer = 10
float_from_int = float(integer)
print(f"float(10) = {float_from_int}")

# String to float
str_float = "10.5"
float_from_string = float(str_float)
print(f"float('10.5') = {float_from_string}")

# Boolean to float
float_from_bool = float(True)
print(f"float(True) = {float_from_bool}")

# Converting to string
print("\n=== Converting to String ===")

# Int to string
number = 10
str_from_int = str(number)
print(f"str(10) = '{str_from_int}' (type: {type(str_from_int).__name__})")

# Float to string
decimal = 3.14
str_from_float = str(decimal)
print(f"str(3.14) = '{str_from_float}'")

# Boolean to string
str_from_bool = str(True)
print(f"str(True) = '{str_from_bool}'")

# List to string
list_data = [1, 2, 3]
str_from_list = str(list_data)
print(f"str([1, 2, 3]) = '{str_from_list}'")

# Converting to boolean
print("\n=== Converting to Boolean ===")

# Int to bool (0 is False, non-zero is True)
bool_from_zero = bool(0)
bool_from_nonzero = bool(10)
print(f"bool(0) = {bool_from_zero}")
print(f"bool(10) = {bool_from_nonzero}")

# String to bool (empty string is False, non-empty is True)
bool_from_empty = bool("")
bool_from_string = bool("Hello")
print(f"bool('') = {bool_from_empty}")
print(f"bool('Hello') = {bool_from_string}")

# Checking type before and after conversion
print("\n=== Type Checking ===")
original = "123"
converted = int(original)

print(f"Original: '{original}' - Type: {type(original).__name__}")
print(f"Converted: {converted} - Type: {type(converted).__name__}")

# Practical example: User input is always string
print("\n=== Practical Example ===")
age_input = "25"  # Simulating user input
age = int(age_input)  # Convert to int for calculation
next_year_age = age + 1
print(f"Current age: {age}")
print(f"Age next year: {next_year_age}")
