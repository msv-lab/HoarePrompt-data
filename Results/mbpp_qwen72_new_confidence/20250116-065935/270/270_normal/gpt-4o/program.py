def cummulative_sum(tuple_list):
    total_sum = 0
    for tup in tuple_list:
        total_sum += sum(tup)
    return total_sum

# Test cases
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
assert cummulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37
assert cummulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44
