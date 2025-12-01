from random import sample

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#$%^&*(){}@"
sample_space = sample(a,10)

password = ""
for sm in sample_space:
    password += sm

print(password)