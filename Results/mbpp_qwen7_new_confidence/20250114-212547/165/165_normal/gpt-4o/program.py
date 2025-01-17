def check_distinct(test_tup):
    return len(test_tup) == len(set(test_tup))

# Testing the function with the provided test cases
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
assert check_distinct((1, 4, 5, 6)) == True
assert check_distinct((2, 3, 4, 5, 6)) == True
