from itertools import combinations

def find_combinations(tuple_list):
    result = []
    for (a, b) in combinations(tuple_list, 2):
        result.append(tuple(x + y for x, y in zip(a, b)))
    return result

# Test cases to validate the solution
assert find_combinations([(1, 2, 3), (3, 4, 5)]) == [(4, 6, 8)]
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
assert find_combinations([(3, 5), (7, 8), (6, 2), (7, 11)]) == [(10, 13), (9, 7), (10, 16), (13, 10), (14, 19), (13, 13)]
assert find_combinations([(4, 6), (8, 9), (7, 3), (8, 12)]) == [(12, 15), (11, 9), (12, 18), (15, 12), (16, 21), (15, 15)]
