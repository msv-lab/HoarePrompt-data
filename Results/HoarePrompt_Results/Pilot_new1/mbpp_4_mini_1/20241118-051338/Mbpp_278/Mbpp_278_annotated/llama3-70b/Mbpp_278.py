def count_first_elements(tup):
    for elem in tup:
        if isinstance(elem, tuple):
            return tup.index(elem)
    return len(tup)
