# write_text_file.py

filename = "output.txt"
text = input("Enter text to write to file: ")

with open(filename, "w") as file:
    file.write(text)

print(f"Text written to {filename}")
