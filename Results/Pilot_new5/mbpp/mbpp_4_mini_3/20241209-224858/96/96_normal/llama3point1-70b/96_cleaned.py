def func_1(tup):
    return len(set((type(x) for x in tup))) == 1