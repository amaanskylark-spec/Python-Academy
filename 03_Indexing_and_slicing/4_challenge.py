# Input an email address (like "student123@gmail.com")
# Slice out the username (everything before '@')
# Remove the first and last character from that username
# Print both: original username and trimmed username

email = input("Enter an email address: ")
at_index = email.index('@') 
username = email[:at_index]
trimmed_username = username[1:-1]
print("Original username:", username)
print("Trimmed username:", trimmed_username)