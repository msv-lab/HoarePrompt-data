def empty_list(N):
    return [{} for _ in range(N)]

# Testing the function with provided test cases
assert empty_list(5) == [{}, {}, {}, {}, {}]
assert empty_list(6) == [{}, {}, {}, {}, {}, {}]
assert empty_list(7) == [{}, {}, {}, {}, {}, {}, {}]
