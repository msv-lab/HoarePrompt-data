def find_combinations(tuples):
    result = []
    for i in range(len(tuples)):
        for j in range(i, len(tuples)):
            combination = tuple(a + b for a, b in zip(tuples[i], tuples[j]))
            result.append(combination)
    return result
