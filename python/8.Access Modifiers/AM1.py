# File: private_example.py

class PrivateClass:
    def __init__(self):
        self.__private_field = "This is a PRIVATE field"

    def __private_method(self):
        print("This is a PRIVATE method")

    def main(self):
        print("Accessing private field in main:", self.__private_field)
        print("Calling private method in main:")
        self.__private_method()

# Subclass trying to access private members
class SubPrivate(PrivateClass):
    def access_private(self):
        print("\nTrying to access private members from subclass:")
        try:
            print(self.__private_field)  # Will raise AttributeError
        except AttributeError:
            print("Cannot access private field!")

        try:
            self.__private_method()  # Will raise AttributeError
        except AttributeError:
            print("Cannot access private method!")

# Run main
obj = PrivateClass()
obj.main()

sub_obj = SubPrivate()
sub_obj.access_private()
