def find_common(arr1, arr2):
    common = []
    for i in arr1:
        for j in arr2:
            if i == j and i not in common:
                common.append(i)
    return common

# Example
print("Common values:", find_common([1, 2, 3, 4], [3, 4, 5, 6]))
