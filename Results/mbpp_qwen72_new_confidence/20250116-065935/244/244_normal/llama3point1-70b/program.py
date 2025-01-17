def find_dissimilar(tup1, tup2):
    return tuple(set(tup1) ^ set(tup2))
