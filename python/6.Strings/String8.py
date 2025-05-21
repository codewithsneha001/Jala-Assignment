# startsWith(), endsWith() and compareTo()
text = "HelloWorld"

# startswith and endswith
print("Starts with 'Hello'?", text.startswith("Hello"))
print("Ends with 'World'?", text.endswith("World"))

# compareTo equivalent
a = "apple"
b = "banana"
if a == b:
    print("Strings are equal")
elif a < b:
    print(f"'{a}' comes before '{b}'")
else:
    print(f"'{a}' comes after '{b}'")
