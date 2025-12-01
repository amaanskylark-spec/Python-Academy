# Input a number
# Use loop to reverse the digits of the number
# Print the reversed number

number = int(input("Enter a number to reverse: "))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print("Reversed number:", reversed_number)