def remove_duplicates(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result

# Example
print("Without duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
