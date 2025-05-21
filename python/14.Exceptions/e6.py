# 6. Create your own exception

class MyCustomError(Exception):
    pass

def test():
    raise MyCustomError("This is my custom error")

try:
    test()
except MyCustomError as e:
    print("Caught:", e)