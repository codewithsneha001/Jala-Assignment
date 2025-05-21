# 2. Handle Arithmetic Exception using try-except block

try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
    print("Cannot divide by zero!")