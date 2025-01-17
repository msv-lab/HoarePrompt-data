def remove_odd(lst):
    return [x for x in lst if x % 2 == 0]

# Tests to verify the function works as expected
assert remove_odd([1,2,3]) == [2]
assert remove_odd([2,4,6]) == [2,4,6]
assert remove_odd([10,20,3]) == [10,20]
