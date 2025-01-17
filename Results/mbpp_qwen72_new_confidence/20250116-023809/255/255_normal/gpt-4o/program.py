def diff_even_odd(nums):
    first_even = None
    first_odd = None
    
    for num in nums:
        if first_even is None and num % 2 == 0:
            first_even = num
        if first_odd is None and num % 2 != 0:
            first_odd = num
        if first_even is not None and first_odd is not None:
            break
    
    if first_even is None or first_odd is None:
        raise ValueError("The list must contain at least one even and one odd number.")
    
    return abs(first_even - first_odd)

# Test cases
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
assert diff_even_odd([1,5,7,9,10])==9
