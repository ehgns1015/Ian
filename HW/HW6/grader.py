class Student:
    """Student class"""
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}  # {course_name: score}
    
    def add_grade(self, course_name, score):
        """Add grade"""
        if 0 <= score <= 100:
            self.grades[course_name] = score
            print(f"Grade registered: {self.name} - {course_name}: {score} points")
        else:
            print("Score must be between 0 and 100.")
    
    def get_average(self):
        """Calculate average score"""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_grade_letter(self):
        """Return letter grade based on average"""
        avg = self.get_average()
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
    
    def display_grades(self):
        """Display grades"""
        print(f"{'='*40}")
        print(f"Student Info: {self.name} (ID: {self.student_id})")
        print(f"{'='*40}")
        if not self.grades:
            print("No grades registered.")
        else:
            for course, score in self.grades.items():
                print(f"{course}: {score} points")
            print(f"{'-'*40}")
            print(f"Average: {self.get_average():.2f} points")
            print(f"Grade: {self.get_grade_letter()}")
        print(f"{'='*40}")


class Course:
    """Course class"""
    def __init__(self, course_name, credit):
        self.course_name = course_name
        self.credit = credit


class GradeManager:
    """Grade management system"""
    def __init__(self):
        self.students = {}  # {student_id: Student object}
        self.courses = {}   # {course_name: Course object}
    
    def add_student(self, student_id, name):
        """Add student"""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} has been added.")
        else:
            print("Student ID already exists.")
    
    def add_course(self, course_name, credit):
        """Add course"""
        if course_name not in self.courses:
            self.courses[course_name] = Course(course_name, credit)
            print(f"Course {course_name} has been added.")
        else:
            print("Course already exists.")
    
    def register_grade(self, student_id, course_name, score):
        """Register grade"""
        if student_id not in self.students:
            print("Student does not exist.")
            return
        if course_name not in self.courses:
            print("Course does not exist.")
            return
        
        self.students[student_id].add_grade(course_name, score)
    
    def show_student_grades(self, student_id):
        """Show grades for specific student"""
        if student_id in self.students:
            self.students[student_id].display_grades()
        else:
            print("Student does not exist.")
    
    def show_all_students(self):
        """Show all students list"""
        print("All Students List:")
        print("-" * 50)
        for student_id, student in self.students.items():
            avg = student.get_average()
            print(f"{student.name} ({student_id}) - Average: {avg:.2f} points, Grade: {student.get_grade_letter()}")
        print("-" * 50 + "")


# Create grade management system
manager = GradeManager()

# Add students
manager.add_student("2024001", "Kim Chulsoo")
manager.add_student("2024002", "Lee Younghee")
manager.add_student("2024003", "Park Minsu")

print()

# Add courses (Middle school subjects)
manager.add_course("Math", 3)
manager.add_course("English", 3)
manager.add_course("Korean", 3)
manager.add_course("Science", 3)
manager.add_course("Social Studies", 3)

print()

# Register grades
manager.register_grade("2025001", "Math", 95)
manager.register_grade("2025001", "English", 88)
manager.register_grade("2025001", "Korean", 92)

print()

manager.register_grade("2025002", "Math", 78)
manager.register_grade("2025002", "English", 85)
manager.register_grade("2025002", "Korean", 82)

print()

manager.register_grade("2025003", "Math", 90)
manager.register_grade("2025003", "Science", 75)

print()

# Show specific student grades
manager.show_student_grades("2025001")
manager.show_student_grades("2025002")
manager.show_student_grades("2025003")

# Show all students
manager.show_all_students()