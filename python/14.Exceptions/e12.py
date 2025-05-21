# 12. Generate NoSuchFieldException (simulate using getattr)

class Student:
    def __init__(self, name):
        self.name = name

obj = Student("Alice")

try:
    print(getattr(obj, 'age'))  # No such attribute
except AttributeError:
    print("NoSuchFieldException: 'age' attribute not found")