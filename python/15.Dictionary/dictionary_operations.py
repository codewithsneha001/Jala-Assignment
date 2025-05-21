# dictionary_operations.py

# 1. Create a Dictionary with at least 5 key-value pairs of Student ID and Name
students = {
    "S101": "Sneha",
    "S102": "Rahul",
    "S103": "Ananya",
    "S104": "Kiran",
    "S105": "Meena"
}
print("1. Initial Dictionary:", students)

# 1.1 Adding a value to the dictionary
students["S106"] = "Vikram"
print("\n1.1 After Adding S106:", students)

# 1.2 Updating a value in the dictionary
students["S102"] = "Ravi"  # Updating 'Rahul' to 'Ravi'
print("\n1.2 After Updating S102:", students)

# 1.3 Accessing a value in the dictionary
print("\n1.3 Name of Student with ID S103:", students["S103"])

# 1.4 Create a nested dictionary
student_details = {
    "S101": {"name": "Sneha", "age": 20, "branch": "IT"},
    "S102": {"name": "Ravi", "age": 21, "branch": "CSE"},
    "S103": {"name": "Ananya", "age": 22, "branch": "ECE"}
}
print("\n1.4 Nested Dictionary:\n", student_details)

# 1.5 Accessing values of nested dictionary
print("\n1.5 Accessing values from Nested Dictionary:")
print(" - Age of S102:", student_details["S102"]["age"])
print(" - Branch of S103:", student_details["S103"]["branch"])

# 1.6 Print the keys in a dictionary
print("\n1.6 Keys in 'students' dictionary:", students.keys())
print("Keys in 'student_details' dictionary:", student_details.keys())

# 1.7 Delete a value from the dictionary
del students["S104"]  # Deleting entry with ID S104
print("\n1.7 After Deleting S104:", students)
