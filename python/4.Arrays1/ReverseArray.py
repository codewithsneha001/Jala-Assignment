def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Example
print("Reversed:", reverse_array([1, 2, 3, 4, 5]))
