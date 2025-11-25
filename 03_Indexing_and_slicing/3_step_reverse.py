# Input a string
# Print the reversed string using slicing
# Print every second character using slicing (step = 2)
# Print characters at even indexes using slicing

input_string = input("Enter a string: ")
reversed_string = input_string[::-1]
every_second_char = input_string[::2]
even_indexed_chars = input_string[0::2]
print("Reversed string:", reversed_string)
print("Every second character:", every_second_char)
print("Characters at even indexes:", even_indexed_chars)