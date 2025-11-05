"""
Numeric Data Types

Python has three numeric types:
1. int - Integer numbers (whole numbers)
2. float - Floating point numbers (decimals)
3. complex - Complex numbers (with real and imaginary parts)

Source: 00_review_and_more.docx - Section 3: Basic Data Types - Numeric Types
"""

# Integer (int)
x = 10
print("Integer:", x)
print("Type:", type(x))

# Negative integer
negative_num = -50
print("\nNegative integer:", negative_num)

# Large integers (Python can handle arbitrarily large integers)
large_num = 123456789012345678901234567890
print("Large integer:", large_num)

# Float
y = 10.5
print("\nFloat:", y)
print("Type:", type(y))

# Float with negative value
negative_float = -3.14
print("Negative float:", negative_float)

# Scientific notation
scientific = 2.5e3  # 2.5 * 10^3 = 2500
print("Scientific notation (2.5e3):", scientific)

small_scientific = 3.7e-3  # 3.7 * 10^-3 = 0.0037
print("Small scientific notation (3.7e-3):", small_scientific)

# Complex number
z = 1 + 2j
print("\nComplex number:", z)
print("Type:", type(z))

# Accessing real and imaginary parts
print("Real part:", z.real)
print("Imaginary part:", z.imag)

# Complex number arithmetic
c1 = 2 + 3j
c2 = 1 - 1j
print("\nComplex addition:", c1 + c2)
print("Complex multiplication:", c1 * c2)

# Numeric operations mixing types
int_num = 5
float_num = 2.5
result = int_num + float_num  # Result is float
print("\nInt + Float:", result)
print("Result type:", type(result))
