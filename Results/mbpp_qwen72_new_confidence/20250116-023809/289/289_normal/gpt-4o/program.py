def is_nonagonal(n):
    return (7 * n * n - 5 * n) // 2

# Test cases
assert is_nonagonal(10) == 325
assert is_nonagonal(15) == 750
assert is_nonagonal(18) == 1089
