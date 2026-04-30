name = input("Enter Name: ")
roll = input("Enter Roll: ")
reg = input("Enter Registration: ")

# Number of subjects
n = int(input("Enter number of subjects: "))

total_points = 0
fail = False

print("\n========== HSC MARKSHEET ==========")
print("Name:", name)
print("Roll:", roll)
print("Registration:", reg)
print("-----------------------------------")
print("Subject        Marks     Grade     Point")

# Loop for subjects
for i in range(n):
    subject = input("\nEnter subject name: ")
    marks = float(input("Enter marks: "))

    # Grade calculation (simple)
    if marks >= 80:
        grade = "A+"
        point = 5.0
    elif marks >= 70:
        grade = "A"
        point = 4.0
    elif marks >= 60:
        grade = "A-"
        point = 3.5
    elif marks >= 50:
        grade = "B"
        point = 3.0
    elif marks >= 40:
        grade = "C"
        point = 2.0
    elif marks >= 33:
        grade = "D"
        point = 1.0
    else:
        grade = "F"
        point = 0.0
        fail = True

    total_points += point

    # Print subject row
    print(subject.ljust(15), str(marks).ljust(10), grade.ljust(10), point)

# GPA calculation
gpa = total_points / n

print("-----------------------------------")

if fail:
    print("Result: FAIL")
    print("GPA: 0.00")
else:
    print("Result: PASS")
    print("GPA:", round(gpa, 2))

print("===================================")