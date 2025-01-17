def unique_sublists(lst):
    sublist_counts = {}
    for sublist in lst:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in sublist_counts:
            sublist_counts[sublist_tuple] += 1
        else:
            sublist_counts[sublist_tuple] = 1
    return sublist_counts
