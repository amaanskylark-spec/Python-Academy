def analyze_string(s):
   total_chars = len(s)
   num_vowels = sum(1 for char in s if char.lower() in 'aeiou')
   num_digits = sum(1 for char in s if char.isdigit())
   num_spaces = sum(1 for char in s if char.isspace())
   return {
          'total_chars': total_chars,
          'num_vowels': num_vowels,
          'num_digits': num_digits,
          'num_spaces': num_spaces
   }

s = input("Enter a string: ")
result = analyze_string(s)
print("Total characters:", result['total_chars'])
print("Number of vowels:", result['num_vowels'])
print("Number of digits:", result['num_digits'])
print("Number of spaces:", result['num_spaces'])