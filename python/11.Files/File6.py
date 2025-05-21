# check_access.py

import os

filename = "sample.txt"

if os.access(filename, os.R_OK):
    print("File has read access")
else:
    print("File does NOT have read access")

if os.access(filename, os.W_OK):
    print("File has write access")
else:
    print("File does NOT have write access")
