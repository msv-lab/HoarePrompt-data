from bisect import bisect_left

def left_insertion(sorted_list, value):
    return bisect_left(sorted_list, value)

# Test cases to verify the solution
assert left_insertion([1,2,4,5],6) == 4
assert left_insertion([1,2,4,5],3) == 2
assert left_insertion([1,2,4,5],7) == 4
