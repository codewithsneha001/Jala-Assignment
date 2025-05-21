def copy_array(arr):
    new_arr = []
    for item in arr:
        new_arr.append(item)
    return new_arr

# Example
original = [10, 20, 30]
copy = copy_array(original)
print("Copied array:", copy)
