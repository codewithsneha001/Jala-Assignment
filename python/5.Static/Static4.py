# 4. Define a static variable and change within the class

class Student:
    school_name = "Bright Future School"

# Changing through class
Student.school_name = "Global Tech Academy"

# Access from class and any instance reflects updated value
s1 = Student()
print("School Name (via class):", Student.school_name)
print("School Name (via instance):", s1.school_name)
