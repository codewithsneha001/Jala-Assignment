def find_index(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

# Example
print("Index of 4:", find_index([10, 20, 30, 40, 50], 40))
