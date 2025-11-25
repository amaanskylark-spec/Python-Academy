def BMI_feedback(bmi):
    feedback = ""
    if bmi < 18.5:
        feedback = "Under Weight"
    elif bmi < 24.9:
        feedback = "Perfect"
    elif bmi < 29.9:
        feedback = "overweight"
    else:
        feedback = "obesity"
    return feedback

def calculate_BMI(weight, height):
    bmi = weight / (height ** 2)
    bmi = round(bmi,2)

    feedback = BMI_feedback(bmi)

    print(f"Your BMI is: {bmi} and you are {feedback}")

w = float(input("Provide weight in Kg: "))
h = float(input("Provide height in meters: "))

calculate_BMI(w,h)
