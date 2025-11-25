# Input a string
# Print first character
# Print last character
# Print middle character (use len() to find middle index)

input_string = input("Enter a string: ")
first_char = input_string[0]
last_char = input_string[-1]
middle_index = len(input_string) // 2
middle_char = input_string[middle_index]
print("First character:", first_char)
print("Last character:", last_char)
print("Middle character:", middle_char)