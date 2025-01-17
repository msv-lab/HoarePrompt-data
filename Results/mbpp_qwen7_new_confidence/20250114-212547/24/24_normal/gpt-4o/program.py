def recursive_list_sum(lst):
    total = 0
    for elem in lst:
        if isinstance(elem, list):
            total += recursive_list_sum(elem)
        else:
            total += elem
    return total

# Test cases
assert recursive_list_sum(([1, 2, [3,4],[5,6]])) == 21
assert recursive_list_sum(([7, 10, [15,14],[19,41]])) == 106
assert recursive_list_sum(([10, 20, [30,40],[50,60]])) == 210
