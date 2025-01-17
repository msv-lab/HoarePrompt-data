def multiple_to_single(lst):
    # Convert each integer in the list to a string and join them
    result_str = ''.join(map(str, lst))
    # Convert the concatenated string back to an integer
    result_int = int(result_str)
    return result_int

# Test cases
assert multiple_to_single([11, 33, 50]) == 113350
assert multiple_to_single([-1, 2, 3, 4, 5, 6]) == -123456
assert multiple_to_single([10, 15, 20, 25]) == 10152025
