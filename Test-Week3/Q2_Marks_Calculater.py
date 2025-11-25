marks = int(input("Enter your marks: "))

if marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B+")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")