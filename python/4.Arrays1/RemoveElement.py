def remove_element(arr, value):
    new_arr = []
    for item in arr:
        if item != value:
            new_arr.append(item)
    return new_arr

# Example
print("After removing 3:", remove_element([1, 2, 3, 4, 3], 3))
print("After removing 2:", remove_element([1, 2, 3, 4, 3], 2))