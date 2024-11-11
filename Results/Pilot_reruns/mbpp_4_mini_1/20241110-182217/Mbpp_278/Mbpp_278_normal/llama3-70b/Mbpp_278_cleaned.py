def func_1(tup):
    for elem in tup:
        if isinstance(elem, tuple):
            return tup.index(elem)
    return len(tup)