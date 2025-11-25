# Input a string
# Print the first 3 characters
# Print the last 3 characters
# Print characters from index 2 to 6

input_string = input("Enter a string: ")
first_three = input_string[:3]
last_three = input_string[-3:]
middle_slice = input_string[2:7]
print("First 3 characters:", first_three)
print("Last 3 characters:", last_three)
print("Characters from index 2 to 6:", middle_slice)