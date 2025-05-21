# Write a program to print largest number among three numbers
a=int(input())
b=int(input())
c=int(input())
if(a>=b and a>=c):
    print("a is greater",a)
if(b>=a and b>=c):
    print("b is greater",b)
if(c>=a and c>=b):
    print("c is greater",c)