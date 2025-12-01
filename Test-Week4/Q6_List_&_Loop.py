numbers = [34, 12, 5, 67, 23, 89, 2, 45, 78, 10]    
largest = numbers[0] 
smallest = numbers[0] 
for num in numbers:
    if num > largest:   
        largest = num 
    if num < smallest:  
        smallest = num  
print(f"Largest number: {largest}") 
print(f"Smallest number: {smallest}")