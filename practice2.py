
name = input("Enter student name: ")
math = float(input("Enter Math grade: "))
physics = float(input("Enter Physics grade: "))
python_grade = float(input("Enter Python grade: "))


average = (math + physics + python_grade) / 3



if average >= 90:
    letter = 'A'
elif average >= 75:
    letter = 'B'
elif average >= 60:
    letter = 'C'
elif average >= 50:
    letter = 'D'
else:
    letter = 'F'


scholarship = average >= 90 and math >= 70 and physics >= 70 and python_grade >= 70


print("=" * 30)
print("Student :", name.upper())
print("Math :", math)
print("Physics :", physics)
print("Python :", python_grade)
print("-" * 30)
print("Average :", average)
print("Letter grade :", letter)
print("Scholarship :", scholarship)
print("=" * 30)




grades = [math, physics, python_grade]
subjects = ['Math', 'Physics', 'Python']

for i in range(len(grades)):
    grade = grades[i]
    
    if grade >= 90:
        comment = "Excellent"
    elif grade >= 75:
        comment = "Good"
    elif grade >= 60:
        comment = "Satisfactory"
    else:
        comment = "Fail"
    
    print(f"{subjects[i]} : {grade} → {comment}")




print("\nName uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))
print("Masked name :", name.replace(name[0], '*', 1))