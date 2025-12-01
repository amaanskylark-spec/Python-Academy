# Input a number n
# Use loop to calculate sum of natural numbers from 1 to n
# Use loop to calculate sum of all odd numbers upto n
# Use loop to calculate sum of all even numbers upto n
# Print all three sums

n = int(input("Enter a natural number: "))
sum_natural = 0
sum_odd = 0
sum_even = 0
for i in range(1, n + 1):
    sum_natural += i
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"Sum of natural numbers from 1 to {n}: {sum_natural}")
print(f"Sum of odd numbers from 1 to {n}: {sum_odd}")
print(f"Sum of even numbers from 1 to {n}: {sum_even}")