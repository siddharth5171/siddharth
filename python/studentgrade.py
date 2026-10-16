m1 = float(input("Enter the marks in subject 1: "))
m2 = float(input("Enter the marks in subject 2: "))
m3 = float(input("Enter the marks in subject 3: "))
m4 = float(input("Enter the marks in subject 4: "))
m5 = float(input("Enter the marks in subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if m1 < 35 or m2 < 35 or m3 < 35 or m4 < 35 or m5 < 35:
    result = "Fail"
    grade = "F"
    print("The student has failed in one or more subjects.")
else:
    result = "Pass"

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "E"

print("The total marks are:", total)
print("The percentage is:", percentage)
print("Grade:", grade)
print("Result:", result)
