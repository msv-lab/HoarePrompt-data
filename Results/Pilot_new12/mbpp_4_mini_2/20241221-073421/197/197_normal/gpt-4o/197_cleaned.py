def func_1(tup, elements):
    count = sum((tup.count(element) for element in elements))
    return count
assert func_1(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3
assert func_1((1, 2, 3, 1, 4, 6, 7, 1, 4), [1, 4, 7]) == 6
assert func_1((1, 2, 3, 4, 5, 6), [1, 2]) == 2