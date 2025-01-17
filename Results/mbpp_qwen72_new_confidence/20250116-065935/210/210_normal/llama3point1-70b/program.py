from itertools import chain, combinations

def combinations_list(lst):
    return list(chain(*map(lambda x: combinations(lst, x), range(0, len(lst) + 1))))
