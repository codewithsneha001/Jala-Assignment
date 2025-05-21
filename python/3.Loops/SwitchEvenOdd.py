num = int(input("Enter a number: "))

match num % 2:
    case 0:
        print(num, "is EVEN")
    case 1:
        print(num, "is ODD")
