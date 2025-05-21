def remove_duplicates_new_array(arr):
    new_array = []
    for num in arr:
        if num not in new_array:
            new_array.append(num)
    return new_array

# Example
print("New array without duplicates:", remove_duplicates_new_array([1, 1, 2, 3, 3, 4]))
