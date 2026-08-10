student_name = input("Enter Student Name: ")
score = int(input("Enter Score: "))

if score >= 70:
    grade = "A"
    display = "Excellent"

elif score >= 60:
    grade = "B"
    display = "Very Good"

elif score >= 50:
    grade = "C"
    display = "Good"

elif score >= 45:
    grade = "D"
    display = "Pass"

elif score >= 40:
    grade = "E"
    display = "Pass"

else:
    grade = "F"
    display = "Fail"

print("\n--- Student Result ---")
print("Student Name:", student_name)
print("Score:", score)
print("Grade:", grade)
print("Display:", display)

if score >= 40:
    print("Congratulations!")
else:
    print("Better Luck Next Time!")
