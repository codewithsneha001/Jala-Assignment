# 5.Throw exception with your own message

def check_age(age):
    if age < 18:
        raise Exception("Age must be at least 18")
    print("Age is valid")

check_age(15)