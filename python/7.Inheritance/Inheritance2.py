# Runtime Polymorphism with Data Members (Instance Variables)
class A:
    var = "A: Variable"

class B(A):
    var = "B: Variable"

class C(B):
    var = "C: Variable"
    
# Main Method for Variables
def main2():
    print("\n--- Data Member Polymorphism ---")
    a = A()
    b = B()
    c = C()

    print("a.var =", a.var)  # A's variable
    print("b.var =", b.var)  # B's variable
    print("c.var =", c.var)  # C's variable

    print("\n--- Access with Superclass Reference ---")
    ref: A

    ref = B()
    print("ref(var from B) =", ref.var)  # Will print A's var because Python doesn't support variable overriding with polymorphism like Java

    ref = C()
    print("ref(var from C) =", ref.var)  # Still prints A's var unless accessed directly from C

main2()
