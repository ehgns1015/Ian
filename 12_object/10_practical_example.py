"""
Practical Application: Student Grade System

A complete example demonstrating OOP concepts:
- Classes and objects
- Instance variables
- Methods
- Lists of objects
- Calculations

Source: Object.docx - Section 9: Practical Application
"""

# Student Grade System
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def highest_grade(self):
        return max(self.grades) if self.grades else 0

    def lowest_grade(self):
        return min(self.grades) if self.grades else 0

    def letter_grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def display_report(self):
        print(f"\n--- Report Card for {self.name} ---")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.average():.2f}")
        print(f"Letter Grade: {self.letter_grade()}")
        print(f"Highest: {self.highest_grade()}")
        print(f"Lowest: {self.lowest_grade()}")

print("=== STUDENT GRADE SYSTEM ===\n")

# Create students
students = [
    Student("Alice", [90, 85, 88, 92]),
    Student("Bob", [70, 78, 80, 75]),
    Student("Charlie", [95, 98, 92, 96]),
    Student("Diana", [60, 65, 58, 70])
]

# Display each student's report
for student in students:
    student.display_report()

# Class statistics
print("\n=== CLASS STATISTICS ===\n")

class_average = sum(s.average() for s in students) / len(students)
print(f"Class average: {class_average:.2f}")

top_student = max(students, key=lambda s: s.average())
print(f"Top student: {top_student.name} ({top_student.average():.2f})")

# Extended example with more features
print("\n\n=== EXTENDED GRADE SYSTEM ===\n")

class ExtendedStudent:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}  # {course_name: [grades]}

    def add_grade(self, course, grade):
        if course not in self.courses:
            self.courses[course] = []
        self.courses[course].append(grade)

    def course_average(self, course):
        if course in self.courses and self.courses[course]:
            return sum(self.courses[course]) / len(self.courses[course])
        return 0

    def gpa(self):
        if not self.courses:
            return 0.0

        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        total_points = 0

        for course, grades in self.courses.items():
            avg = self.course_average(course)
            if avg >= 90:
                letter = 'A'
            elif avg >= 80:
                letter = 'B'
            elif avg >= 70:
                letter = 'C'
            elif avg >= 60:
                letter = 'D'
            else:
                letter = 'F'
            total_points += grade_points[letter]

        return total_points / len(self.courses)

    def display_transcript(self):
        print(f"\n{'='*50}")
        print(f"TRANSCRIPT - {self.name} (ID: {self.student_id})")
        print(f"{'='*50}")

        for course, grades in self.courses.items():
            avg = self.course_average(course)
            print(f"\n{course}:")
            print(f"  Grades: {grades}")
            print(f"  Average: {avg:.2f}")

        print(f"\n{'='*50}")
        print(f"GPA: {self.gpa():.2f}")
        print(f"{'='*50}")

# Create extended student
student = ExtendedStudent("S001", "Emily")

# Add grades for multiple courses
student.add_grade("Math", 85)
student.add_grade("Math", 90)
student.add_grade("Math", 88)

student.add_grade("Science", 92)
student.add_grade("Science", 88)
student.add_grade("Science", 95)

student.add_grade("English", 78)
student.add_grade("English", 82)
student.add_grade("English", 80)

# Display transcript
student.display_transcript()

# Complete classroom system
print("\n\n=== COMPLETE CLASSROOM SYSTEM ===\n")

class ClassRoom:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0
        total = sum(s.average() for s in self.students)
        return total / len(self.students)

    def display_summary(self):
        print(f"\n{'='*50}")
        print(f"COURSE: {self.course_name}")
        print(f"TEACHER: {self.teacher}")
        print(f"{'='*50}")

        for student in self.students:
            print(f"{student.name}: {student.average():.2f} ({student.letter_grade()})")

        print(f"{'='*50}")
        print(f"Class Average: {self.class_average():.2f}")
        print(f"{'='*50}")

# Create classroom
classroom = ClassRoom("Python Programming", "Dr. Smith")

# Add students
classroom.add_student(Student("Alice", [90, 85, 88]))
classroom.add_student(Student("Bob", [70, 78, 80]))
classroom.add_student(Student("Charlie", [95, 98, 92]))

# Display classroom summary
classroom.display_summary()

# Additional practical features
print("\n\n=== ADDITIONAL FEATURES ===\n")

class AdvancedStudent(Student):
    def __init__(self, name, grades, attendance):
        super().__init__(name, grades)
        self.attendance = attendance  # Percentage

    def is_passing(self):
        return self.average() >= 60 and self.attendance >= 75

    def display_status(self):
        print(f"\n{self.name}:")
        print(f"  Average: {self.average():.2f}")
        print(f"  Attendance: {self.attendance}%")
        print(f"  Status: {'PASS' if self.is_passing() else 'FAIL'}")

# Test advanced features
adv_students = [
    AdvancedStudent("Frank", [75, 80, 78], 90),
    AdvancedStudent("Grace", [85, 88, 82], 65),
    AdvancedStudent("Henry", [55, 60, 58], 80)
]

for student in adv_students:
    student.display_status()

# Summary
print("\n=== OOP CONCEPTS DEMONSTRATED ===\n")
print("✓ Classes and Objects")
print("✓ Instance Variables")
print("✓ Methods")
print("✓ Lists of Objects")
print("✓ Calculations and Logic")
print("✓ Inheritance")
print("✓ Object Composition")
print("✓ Real-world Application")
