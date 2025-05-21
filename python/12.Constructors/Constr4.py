class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

if __name__ == "__main__":
    p = Person("Alice", 25)
    p.display()
