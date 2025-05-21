# 7. Program with finally block

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Caught division by zero")
finally:
    print("Finally block always executes")
