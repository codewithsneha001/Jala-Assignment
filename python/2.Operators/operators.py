#Arithmetic Operators
def arithmetic_operations(a, b):
    print("Arithmetic Operators(+,-,*,/)\n")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b if b != 0 else "Cannot divide by zero")

# Example usage
arithmetic_operations(10, 5)


# increment/decrement operators
def increment_decrement():
    print("\nIncrement/Decrement operators(++,--)\n")
    num = 10
    print("Original:", num)
    
    num += 1  # Increment
    print("After Increment:", num)
    
    num -= 1  # Decrement
    print("After Decrement:", num)

increment_decrement()

# Equal or not
def check_equality(x, y):
    print("\nEqual or Not(==,!=)\n")
    if x == y:
        print("The numbers are equal.",x,y)
    else:
        print("The numbers are not equal.",x,y)

check_equality(10, 10)
check_equality(10, 5)

# Relational Operators (<, <=, >, >=)
def relational_operators(a, b):
    print("\nRelational Operators(<, <=, >, >=)\n")
    print("a < b:", a < b,a,b,a,b)
    print("a <= b:", a <= b,a,b)
    print("a > b:", a > b,a,b)
    print("a >= b:", a >= b,a,b)

relational_operators(10, 5)

# Smaller and Larger Number
def find_smaller_larger(x, y):
    print("\nSmaller and larger numbers\n")
    smaller = min(x, y)
    larger = max(x, y)
    print("Smaller number:", smaller)
    print("Larger number:", larger)

find_smaller_larger(25, 42)

