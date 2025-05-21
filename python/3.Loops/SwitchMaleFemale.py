gender = input("Enter gender (M/F): ")

match gender.upper():
    case "M":
        print("Gender: Male")
    case "F":
        print("Gender: Female")
    case _:
        print("Invalid input")
