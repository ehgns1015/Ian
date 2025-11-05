"""
If-Elif-Else Statement

The elif (else if) statement allows you to check multiple conditions.
Python checks each condition in order and executes the first matching block.

Source: 00_review_and_more.docx - Section 11: Conditional Statements - if-elif-else Statement
"""

# Basic if-elif-else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Multiple elif statements
age = 15

if age < 13:
    category = "Child"
elif age < 18:
    category = "Teenager"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"

print(f"Age: {age}, Category: {category}")

# If-elif-else with comparisons
temperature = 25

if temperature < 0:
    print("Freezing")
elif temperature < 10:
    print("Cold")
elif temperature < 20:
    print("Cool")
elif temperature < 30:
    print("Warm")
else:
    print("Hot")

# If-elif-else with string matching
day = "Monday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
elif day == "Friday":
    print("Almost weekend!")
else:
    print("Weekday")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: BMI Calculator
weight = 70  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)

print(f"BMI: {bmi:.2f}")
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

# Example 2: Traffic light
light = "yellow"

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Caution")
elif light == "green":
    print("Go")
else:
    print("Invalid light color")

# Example 3: Ticket pricing
age = 25

if age < 5:
    price = 0
    print("Free (under 5)")
elif age < 18:
    price = 10
    print("Child ticket: $10")
elif age < 65:
    price = 20
    print("Adult ticket: $20")
else:
    price = 15
    print("Senior ticket: $15")

# Example 4: Grade with plus/minus
score = 87

if score >= 97:
    grade = "A+"
elif score >= 93:
    grade = "A"
elif score >= 90:
    grade = "A-"
elif score >= 87:
    grade = "B+"
elif score >= 83:
    grade = "B"
elif score >= 80:
    grade = "B-"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"\nScore: {score}, Grade: {grade}")

# Example 5: Month days
month = "February"
year = 2024  # Leap year

if month in ["January", "March", "May", "July", "August", "October", "December"]:
    days = 31
elif month in ["April", "June", "September", "November"]:
    days = 30
elif month == "February":
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days = 29  # Leap year
    else:
        days = 28
else:
    days = 0
    print("Invalid month")

if days > 0:
    print(f"{month} {year} has {days} days")

# Example 6: Shipping cost
weight = 2.5  # kg
distance = 150  # km

if weight <= 1:
    base_cost = 5
elif weight <= 5:
    base_cost = 10
elif weight <= 10:
    base_cost = 20
else:
    base_cost = 30

if distance <= 50:
    distance_cost = 2
elif distance <= 100:
    distance_cost = 5
else:
    distance_cost = 10

total_cost = base_cost + distance_cost
print(f"\nShipping: {weight}kg, {distance}km")
print(f"Total cost: ${total_cost}")

# Example 7: Temperature recommendation
temp = 22

if temp < 0:
    print("\nWear heavy winter coat")
elif temp < 10:
    print("\nWear warm jacket")
elif temp < 20:
    print("\nWear light jacket")
elif temp < 30:
    print("\nWear t-shirt")
else:
    print("\nWear light clothes and stay hydrated")
