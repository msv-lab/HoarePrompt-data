def split_two_parts(lst, L):
    return (lst[:L], lst[L:])

# Tests
assert split_two_parts([1,1,2,3,4,4,5,1],3) == ([1, 1, 2], [3, 4, 4, 5, 1])
assert split_two_parts(['a', 'b', 'c', 'd'],2) == (['a', 'b'], ['c', 'd'])
assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4) == (['p', 'y', 't', 'h'], ['o', 'n'])
