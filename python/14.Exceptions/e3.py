# 3. Method that throws exception, call without try block

def risky_method():
    raise ValueError("This is a risky method")

risky_method()  # No try block, raises ValueError