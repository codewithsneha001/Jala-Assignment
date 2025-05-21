def count_even_odd(arr):
    even = 0
    odd = 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

# Example
even_count, odd_count = count_even_odd([1, 2, 3, 4, 5, 6])
print("Even:", even_count, "Odd:", odd_count)
