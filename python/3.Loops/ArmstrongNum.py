# Write a program to find Armstrong number or not
# Generalized Armstrong Number Checker

num = int(input("Enter a number: "))
num_digits = len(str(num))  # Count the number of digits
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")