def tuple_intersection(list1, list2):
    return set(tuple(sorted(t)) for t in list1) & set(tuple(sorted(t)) for t in list2)
