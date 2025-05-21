# 10. Simulate ClassNotFoundException (not in Python, use import error)

try:
    import nonexistentmodule
except ModuleNotFoundError as e:
    print("Caught ModuleNotFoundError:", e)