def contains_elements(arr, val1, val2):
    found1 = found2 = False
    for num in arr:
        if num == val1:
            found1 = True
        if num == val2:
            found2 = True
    return found1 and found2

# Example
print("Contains 12 and 23?", contains_elements([10, 12, 20, 23, 25], 12, 23))
