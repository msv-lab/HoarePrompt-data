def find_star_num(n):
    return 6 * n * (n - 1) + 1

# Test cases
assert find_star_num(3) == 37
assert find_star_num(4) == 73
assert find_star_num(5) == 121
