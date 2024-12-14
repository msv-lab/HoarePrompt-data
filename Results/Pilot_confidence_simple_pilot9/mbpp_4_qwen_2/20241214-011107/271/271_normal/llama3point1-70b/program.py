def average_tuple(tuples):
    return [sum(val) / len(tuples) for val in zip(*tuples)]
