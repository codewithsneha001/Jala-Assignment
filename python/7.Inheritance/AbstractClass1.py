
#1
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def non_abstract_method(self):
        print("This is a NON-abstract method from AbstractClass")

    @abstractmethod
    def abstract_method(self):
        pass
#2
class ChildClass(AbstractClass):
    def abstract_method(self):
        print("Abstract method implemented in ChildClass")

    def main_access_abstract(self):
        print("\nCalling abstract and non-abstract methods from ChildClass:")
        self.abstract_method()
        self.non_abstract_method()

#3 and 4
# Calling in main
if __name__ == "__main__":
    child = ChildClass()
    print("Calling non-abstract method using AbstractClass reference:")
    abstract_ref = child  # AbstractClass reference
    abstract_ref.non_abstract_method()

    print("\nCreating object in child class to call abstract and non-abstract methods:")
    child.main_access_abstract()
