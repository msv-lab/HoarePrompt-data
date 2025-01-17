def interleave_lists(list1, list2, list3):
    return [x for tup in zip(list1, list2, list3) for x in tup]
