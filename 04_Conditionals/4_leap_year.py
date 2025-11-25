# Input a year
# Check if divisible by 4
# Print if leap year or not

year = int(input("Enter a year: "))
if (year % 4) == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")