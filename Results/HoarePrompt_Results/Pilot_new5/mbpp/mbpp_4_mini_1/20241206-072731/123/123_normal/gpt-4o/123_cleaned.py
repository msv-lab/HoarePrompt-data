def func_1(lst, L):
    return (lst[:L], lst[L:])
assert func_1([1, 1, 2, 3, 4, 4, 5, 1], 3) == ([1, 1, 2], [3, 4, 4, 5, 1])
assert func_1(['a', 'b', 'c', 'd'], 2) == (['a', 'b'], ['c', 'd'])
assert func_1(['p', 'y', 't', 'h', 'o', 'n'], 4) == (['p', 'y', 't', 'h'], ['o', 'n'])