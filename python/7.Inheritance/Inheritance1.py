# Using Methods (Polymorphism with Methods)
# Superclass A
class A:
    def feature1(self):
        print("A: Feature 1")

    def feature2(self):
        print("A: Feature 2")

    def common(self):
        print("A: Common method")

# Subclass B of A
class B(A):
    def feature3(self):
        print("B: Feature 3")

    def feature4(self):
        print("B: Feature 4")

    def common(self):
        print("B: Common method (Overridden)")

# Subclass C of B
class C(B):
    def feature5(self):
        print("C: Feature 5")

    def feature6(self):
        print("C: Feature 6")

    def common(self):
        print("C: Common method (Overridden)")
        
# Main Method (Driver Code)
def main():
    print("--- Object of A ---")
    a = A()
    a.feature1()
    a.feature2()
    a.common()

    print("\n--- Object of B ---")
    b = B()
    b.feature1()
    b.feature2()
    b.feature3()
    b.feature4()
    b.common()

    print("\n--- Object of C ---")
    c = C()
    c.feature1()
    c.feature2()
    c.feature3()
    c.feature4()
    c.feature5()
    c.feature6()
    c.common()

    print("\n--- Polymorphism with Superclass Reference ---")
    ref: A

    ref = B()
    ref.common()  # Calls B's common()

    ref = C()
    ref.common()  # Calls C's common()

main()
