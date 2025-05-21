def min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

# Example
min_val, max_val = min_max([7, 2, 9, 4, 1])
print("Min:", min_val, "Max:", max_val)
