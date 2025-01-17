def centered_hexagonal_number(n):
    return 3 * n * (n - 1) + 1

# Testing the function with the provided test cases
assert centered_hexagonal_number(10) == 271
assert centered_hexagonal_number(2) == 7
assert centered_hexagonal_number(9) == 217
