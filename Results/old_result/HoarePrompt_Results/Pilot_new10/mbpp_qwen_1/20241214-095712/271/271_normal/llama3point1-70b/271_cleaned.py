def func_1(tuples):
    return [sum(val) / len(tuples) for val in zip(*tuples)]