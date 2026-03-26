name = input("Enter student name: ")
math = float(input("Enter Math grade: "))
physics = float(input("Enter Physics grade: "))
python_grade = float(input("Enter Python grade: "))

average = (math + physics + python_grade) / 3
scholarship = 35000 if average >= 90 else 0
gpa = average / 25

print("=" * 30)
print("STUDENT REPORT CARD")
print("=" * 30)
print("Student :", name)
print("Math :", math)
print("Physics :", physics)
print("Python :", python_grade)
print("-" * 30)
print("Average :", round(average, 2))
print("GPA :", round(gpa, 2))
print("Scholarship :", scholarship, "KZT")
print("=" * 30)

print("Scholarship granted:", average >= 90)
print("Perfect score:", average == 100)