def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

# Example
print("Duplicates:", find_duplicates([1, 2, 3, 2, 4, 1, 5, 3]))
