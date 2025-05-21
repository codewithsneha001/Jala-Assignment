class AccessModifiers:
    def __init__(self):
        print("Public constructor")

    def _protected_constructor(self):
        print("Protected constructor (by convention)")

    def __private_constructor(self):
        print("Private constructor (name mangling)")

    def default_constructor(self):
        print("Default constructor (no explicit modifier)")

obj = AccessModifiers()
obj._protected_constructor()
obj.default_constructor()
# obj.__private_constructor()  # Will raise AttributeError

# Access private method via name mangling
obj._AccessModifiers__private_constructor()
