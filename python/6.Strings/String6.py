# Matching a String Against a Regular Expression With matches()
import re

text = "Python123"
pattern = "^[A-Za-z0-9]+$"  # Alphanumeric check

if re.match(pattern, text):
    print("String matches the pattern")
else:
    print("String does not match the pattern")
