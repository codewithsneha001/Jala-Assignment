class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default constructor")
        elif b is None:
            print(f"One argument constructor: a = {a}")
        else:
            print(f"Two argument constructor: a = {a}, b = {b}")

    @classmethod
    def one_arg_constructor(cls, a):
        return cls(a)

    @classmethod
    def two_arg_constructor(cls, a, b):
        return cls(a, b)

class MainClass:
    @staticmethod
    def main():
        obj1 = MyClass()
        obj2 = MyClass.one_arg_constructor(10)
        obj3 = MyClass.two_arg_constructor(20, 30)

if __name__ == "__main__":
    MainClass.main()
