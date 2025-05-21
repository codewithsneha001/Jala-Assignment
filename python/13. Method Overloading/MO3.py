# 3. Methods with Same Name and Same Number of Parameters of Same Type (Simulated)
class Operation:
    def action(self, a, b):
        if a > b:
            print("First is greater")
        elif a < b:
            print("Second is greater")
        else:
            print("Both are equal")

op = Operation()
op.action(5, 3)
op.action(2, 7)
op.action(4, 4)
