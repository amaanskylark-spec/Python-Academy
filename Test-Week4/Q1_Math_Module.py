import math

number = int(input("Enter a number: "))
square = int(math.pow(number, 2))
cube = int(math.pow(number, 3))
square_root = round(math.sqrt(number), 2) 
print(f"Square of {number} is {square}")
print(f"Cube of {number} is {cube}")
print(f"Square root of {number} is {square_root}")