# Take two numbers as input
# Store one value in temp
# Swap the variables
# Print before and after swapping

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
temp = num1
num1 = num2
num2 = temp
print(f"After swapping: num1 = {num1}, num2 = {num2}")