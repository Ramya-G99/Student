print("=== Student Grade Calculator ===")

name = input("Enter Student Name: ")
marks = int(input("Enter Marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)