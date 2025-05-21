def second_largest(arr):
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

# Example
print("Second largest:", second_largest([10, 20, 5, 25, 15]))
