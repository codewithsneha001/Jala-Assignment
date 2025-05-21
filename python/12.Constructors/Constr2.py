class SuperClass:
    def __init__(self, a=None):
        if a is None:
            print("SuperClass default constructor")
        else:
            print(f"SuperClass parameterized constructor with a={a}")

class ChildClass(SuperClass):
    def __init__(self, a=None):
        if a is None:
            super().__init__()
            print("ChildClass default constructor")
        else:
            super().__init__(a)
            print(f"ChildClass parameterized constructor with a={a}")

if __name__ == "__main__":
    c1 = ChildClass()
    c2 = ChildClass(100)
