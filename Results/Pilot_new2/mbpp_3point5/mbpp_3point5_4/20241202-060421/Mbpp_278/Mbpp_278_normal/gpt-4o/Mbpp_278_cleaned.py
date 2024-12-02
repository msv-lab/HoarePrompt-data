def func_1(tup):
    count = 0
    for elem in tup:
        if isinstance(elem, tuple):
            break
        count += 1
    return count
assert func_1((1, 5, 7, (4, 6), 10)) == 3
assert func_1((2, 9, (5, 7), 11)) == 2
assert func_1((11, 15, 5, 8, (2, 3), 8)) == 4