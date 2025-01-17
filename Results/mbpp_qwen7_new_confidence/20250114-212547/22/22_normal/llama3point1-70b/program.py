def max_difference(tuples):
    return max(max(t) - min(t) for t in tuples)
