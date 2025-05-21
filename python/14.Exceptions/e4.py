# 4. Multiple except blocks
try:
    a = int("abc")
    b = 10 / 0
except ValueError:
    print("ValueError: Invalid input")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")