import math

def catalan_number(n):
    return math.comb(2 * n, n) // (n + 1)

# Tests
assert catalan_number(10) == 16796
assert catalan_number(9) == 4862
assert catalan_number(7) == 429
