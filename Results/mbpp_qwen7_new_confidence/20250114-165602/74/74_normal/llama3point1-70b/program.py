def max_occurrences(lst):
    return max(set(lst), key=lst.count)
