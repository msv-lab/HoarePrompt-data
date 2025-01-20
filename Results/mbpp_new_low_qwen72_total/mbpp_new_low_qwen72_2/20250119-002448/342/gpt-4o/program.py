def mul_even_odd(lst):
    first_odd = None
    first_even = None
    
    for num in lst:
        if first_odd is None and num % 2 != 0:
            first_odd = num
        if first_even is None and num % 2 == 0:
            first_even = num
        if first_odd is not None and first_even is not None:
            break
    
    return first_odd * first_even

# Test cases
assert mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 4
assert mul_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
assert mul_even_odd([1, 5, 7, 9, 10]) == 10
