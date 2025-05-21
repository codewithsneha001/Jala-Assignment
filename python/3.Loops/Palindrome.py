# Palindrome check without using str() or reversed()

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")
