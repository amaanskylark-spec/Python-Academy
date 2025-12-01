import random

random_numbers = []
for i in range(5):
    random_numbers.append(random.randint(1, 50))
print("Random Numbers:", random_numbers)
print("Sum of Numbers:", sum(random_numbers))