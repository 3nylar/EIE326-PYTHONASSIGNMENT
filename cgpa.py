# GPA Calculator for 6 Courses with User Input

def get_grade_point(score):
    if score >= 70:
        return 5  # A
    elif score >= 60:
        return 4  # B
    elif score >= 50:
        return 3  # C
    elif score >= 45:
        return 2  # D
    elif score >= 40:
        return 1  # E
    else:
        return 0  # F

total_quality_points = 0
total_units = 0

print("CGPA CALCULATOR FOR 6 COURSES\n")

for i in range(1, 7):
    print(f"--- Course {i} ---")
    course_name = input("Enter course name: ")
    score = int(input("Enter your score: "))
    unit = int(input("Enter course unit: "))
    
    grade_point = get_grade_point(score)
    quality_point = grade_point * unit
    
    total_quality_points += quality_point
    total_units += unit

gpa = total_quality_points / total_units if total_units > 0 else 0
print(f"\nYour CGPA for 6 courses is: {round(gpa, 2)}")
