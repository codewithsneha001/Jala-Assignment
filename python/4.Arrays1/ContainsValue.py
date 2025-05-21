def contains_value(arr, value):
    for item in arr:
        if item == value:
            return True
    return False

# Example
print("Contains 3?", contains_value([1, 2, 3, 4], 3))
print("Contains 5?", contains_value([1, 2, 3, 4], 5))
