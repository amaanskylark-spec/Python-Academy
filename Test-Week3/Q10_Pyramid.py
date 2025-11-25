n = int(input("Enter the height of the pyramid: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i) 
total_sum = sum(range(1, n + 1))    
print(f"The sum of all numbers from 1 to {n} is: {total_sum}")