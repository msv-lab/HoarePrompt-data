def add_pairwise(tup):
    return tuple(a + b for a, b in zip(tup, tup[1:]))
