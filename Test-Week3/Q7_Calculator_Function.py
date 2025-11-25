num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
operator = input("Enter Operation You want to perform+,-,*,/,%:")
def calculator(n1, n2, op):
    match op:
        case "+":
            print(f"{n1} + {n2} = {n1 + n2}")
        case "-":
            print(f"{n1} - {n2} = {n1 - n2}")
        case "*":
            print(f"{n1} * {n2} = {n1 * n2}")
        case "/":
            print(f"{n1} / {n2} = {n1 / n2}")
        case "%":
            print(f"{n1} % {n2} = {n1 % n2}")
        case _:
            print("Invalid Operation")
calculator(num1, num2, operator)