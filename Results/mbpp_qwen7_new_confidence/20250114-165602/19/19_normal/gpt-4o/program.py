def is_octagonal(n: int) -> int:
    return n * (3 * n - 2)

# Test cases to validate the solution
assert is_octagonal(5) == 65
assert is_octagonal(10) == 280
assert is_octagonal(15) == 645
