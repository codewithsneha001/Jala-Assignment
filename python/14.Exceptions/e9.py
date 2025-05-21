# 9. Generate FileNotFoundError

with open("nonexistent.txt", "r") as f:
    data = f.read()  # FileNotFoundError