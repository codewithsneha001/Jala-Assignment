def insert_at_position(arr, value, position):
    new_arr = []
    for i in range(len(arr)):
        if i == position:
            new_arr.append(value)
        new_arr.append(arr[i])
    if position >= len(arr):  # If position is at end
        new_arr.append(value)
    return new_arr

# Example
print("After insertion:", insert_at_position([1, 2, 4, 5], 3, 2))
