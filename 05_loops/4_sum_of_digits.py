# Input a number
# Use loop to extract digits (using % and //)
# Maintain sum of digits
# Maintain product of digits
# Print both values

number = int(input("Enter a number: "))
sum_of_digits = 0
product_of_digits = 1
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    product_of_digits *= digit
    number //= 10
print("Sum of digits:", sum_of_digits)
print("Product of digits:", product_of_digits)