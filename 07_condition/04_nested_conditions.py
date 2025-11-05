"""
Nested Conditional Statements

Nested conditions are if statements inside other if statements.
Useful for checking multiple conditions that depend on each other.

Source: 00_review_and_more.docx - Section 11: Conditional Statements - Nested Conditionals
"""

# Basic nested if
age = 25
has_license = True

if age >= 18:
    print("Age requirement met")
    if has_license:
        print("You can drive")
    else:
        print("You need to get a license first")
else:
    print("You are too young to drive")

# Nested if-else
number = 15

if number > 0:
    print(f"{number} is positive")
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
else:
    print(f"{number} is not positive")

# Multiple levels of nesting
score = 85
attendance = 90

if score >= 60:
    print("Passed the exam")
    if attendance >= 75:
        print("Attendance requirement met")
        if score >= 90 and attendance >= 90:
            print("Award: Excellence!")
        elif score >= 80:
            print("Award: Merit")
        else:
            print("Award: Pass")
    else:
        print("Attendance too low")
else:
    print("Failed the exam")

# Nested conditions with logical operators
username = "admin"
password = "secret123"
is_active = True

if username == "admin":
    if password == "secret123":
        if is_active:
            print("Login successful")
        else:
            print("Account is deactivated")
    else:
        print("Incorrect password")
else:
    print("Username not found")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Loan eligibility
age = 30
income = 50000
credit_score = 720
has_job = True

if age >= 21:
    if has_job:
        if income >= 30000:
            if credit_score >= 650:
                print("Loan approved!")
                if credit_score >= 750:
                    interest_rate = 3.5
                elif credit_score >= 700:
                    interest_rate = 4.5
                else:
                    interest_rate = 5.5
                print(f"Interest rate: {interest_rate}%")
            else:
                print("Credit score too low")
        else:
            print("Income too low")
    else:
        print("Employment required")
else:
    print("Must be 21 or older")

# Example 2: Shipping calculation
country = "USA"
weight = 2.5
is_express = True

if country == "USA":
    print("Domestic shipping")
    if weight <= 1:
        cost = 5
    elif weight <= 5:
        cost = 10
    else:
        cost = 20

    if is_express:
        cost *= 2
        print("Express shipping")

    print(f"Shipping cost: ${cost}")
else:
    print("International shipping rates apply")

# Example 3: Restaurant discount
is_member = True
purchase = 150
day = "Tuesday"

if is_member:
    print("Member discount applied")
    if day == "Tuesday":
        discount = 0.20  # 20% discount on Tuesday
        print("Extra Tuesday discount!")
    else:
        discount = 0.10  # 10% regular member discount

    if purchase >= 100:
        discount += 0.05  # Additional 5% for large purchase
        print("Large purchase bonus!")

    final_price = purchase * (1 - discount)
    print(f"Total discount: {discount * 100}%")
    print(f"Final price: ${final_price:.2f}")
else:
    print(f"Price: ${purchase}")
    print("Sign up for membership to get discounts!")

# Example 4: Grade with conditions
has_exam = True
exam_score = 85
has_project = True
project_score = 90
attendance_rate = 88

if has_exam:
    if exam_score >= 60:
        print("Exam passed")
        if has_project:
            if project_score >= 70:
                print("Project passed")
                if attendance_rate >= 80:
                    final_grade = (exam_score * 0.6 + project_score * 0.4)
                    print(f"Final grade: {final_grade:.2f}")
                    if final_grade >= 90:
                        print("Excellent!")
                    elif final_grade >= 80:
                        print("Very good!")
                    else:
                        print("Good!")
                else:
                    print("Attendance too low")
            else:
                print("Project score insufficient")
        else:
            print("Project not submitted")
    else:
        print("Exam failed")
else:
    print("Exam not taken")

# Example 5: Access control
is_authenticated = True
user_role = "admin"
resource = "user_data"

if is_authenticated:
    print("User authenticated")
    if user_role == "admin":
        print("Admin access granted")
        print(f"Accessing {resource}...")
    elif user_role == "editor":
        if resource in ["articles", "posts"]:
            print(f"Editor can access {resource}")
        else:
            print("Access denied for this resource")
    else:
        if resource == "public_data":
            print("Public access granted")
        else:
            print("Access denied")
else:
    print("Please log in")
