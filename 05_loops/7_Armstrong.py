number = int(input("Enter a number to check if it's an Armstrong number: "))
original_number = number
sum_of_cubes = 0
while number > 0:
    digit = number % 10
    sum_of_cubes += digit ** 3
    number //= 10
if original_number == sum_of_cubes:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")