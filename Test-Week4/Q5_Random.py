import random

num = random.randint(1,10)

UserEntered = int(input("Enter a number between 1 and 10: "))

if UserEntered == num:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the correct number is {num}. Better luck next time!")