# Input a number n
# Use a loop to print numbers from 1 to n
# Use another loop to print numbers from n to 1 (reverse order)

n = int(input("Enter a natural number: "))
print("Numbers from 1 to", n)
for i in range(1, n + 1):
    print(i, end=' ')
print("\nNumbers from", n, "to 1")
for i in range(n, 0, -1):
    print(i, end=' ')
print()  