# read_seek.py

with open("sample.txt", "r") as file:
    file.seek(5)  # Skip first 5 characters
    print("Reading from 5th character onward:")
    print(file.read())
