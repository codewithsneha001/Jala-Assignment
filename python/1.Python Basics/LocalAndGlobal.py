value = 100  # Global variable

def main():
    value = 50  # Local variable with the same name
    print("Local value:", value)
    print("Global value:", globals()['value'])  # Accessing global value

main()
