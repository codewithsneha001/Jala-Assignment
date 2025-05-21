# File: protected_example.py

class ProtectedClass:
    def __init__(self):
        self._protected_field = "This is a PROTECTED field"

    def _protected_method(self):
        print("This is a PROTECTED method")

# Another class in same file (same package)
class SamePackageAccess:
    def access(self):
        obj = ProtectedClass()
        print("Accessing protected field:", obj._protected_field)
        obj._protected_method()

# Child class in same or different file (package simulation in Python)
class SubProtected(ProtectedClass):
    def access(self):
        print("Accessing protected field from subclass:", self._protected_field)
        self._protected_method()

# Run access
print("\n--- Protected Access from Same Package ---")
same = SamePackageAccess()
same.access()

print("\n--- Protected Access from Subclass ---")
sub = SubProtected()
sub.access()
