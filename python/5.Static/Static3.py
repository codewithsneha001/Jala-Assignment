
# 3. Define a static variable and change within the instance

class Student:
    school_name = "Bright Future School"

s1 = Student()
s1.school_name = "Success Academy"  # This creates an instance variable, does NOT change static variable

print("School Name (via instance):", s1.school_name)         # New value for s1
print("School Name (via class):", Student.school_name)       # Original static value remains unchanged
