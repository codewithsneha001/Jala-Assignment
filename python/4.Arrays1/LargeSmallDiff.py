def difference_largest_smallest(arr):
    min_val = max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return max_val - min_val

# Example
print("Difference:", difference_largest_smallest([5, 1, 9, 3, 7]))
