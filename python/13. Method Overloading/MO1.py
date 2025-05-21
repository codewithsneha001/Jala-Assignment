# 1. Methods with Same Name but Different Number of Parameters (Same Type)

class Calculator:
    def add(self, a, b, c=0):  # third parameter is optional
        return a + b + c

calc = Calculator()
print("Sum of 2 numbers:", calc.add(10, 20))
print("Sum of 3 numbers:", calc.add(10, 20, 30))