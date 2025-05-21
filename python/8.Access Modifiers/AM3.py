# File: public_example.py

class PublicClass:
    def __init__(self):
        self.public_field = "This is a PUBLIC field"

    def public_method(self):
        print("This is a PUBLIC method")

# Access from anywhere (same/different module)
class AccessPublic:
    def access(self):
        obj = PublicClass()
        print("Accessing public field:", obj.public_field)
        obj.public_method()

# Run access
print("\n--- Public Access from Anywhere ---")
access = AccessPublic()
access.access()
