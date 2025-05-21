# Write a program to print the odd and even numbers
num=int(input())
for i in range(1, num+1):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")