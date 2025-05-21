#  2. Methods with Same Name but Different Number of Parameters of Different Data Type

class Display:
    def show(self, a, b=None):
        if b is None:
            print("String:", a)
        elif isinstance(a, int) and isinstance(b, int):
            print("Sum of integers:", a + b)
        elif isinstance(a, float) and isinstance(b, float):
            print("Sum of floats:", a + b)
        else:
            print("Unsupported types")

disp = Display()
disp.show("Hello")
disp.show(10, 20)
disp.show(3.5, 2.5)