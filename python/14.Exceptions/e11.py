# 11. Generate IOError

try:
    with open("/root/lockedfile.txt", "r") as f:
        data = f.read()
except IOError as e:
    print("Caught IOError:", e)