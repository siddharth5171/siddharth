# Prompt user for input and convert to a decimal number
try:
    score = float(input("Enter the student's score (0-100): "))

    # Validate the score range
    if score < 0 or score > 100:
        print("Error: Score must be between 0 and 100.")
    # Conditional logic to assign grades
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
        
except ValueError:
    print("Error: Please enter a valid number.")
