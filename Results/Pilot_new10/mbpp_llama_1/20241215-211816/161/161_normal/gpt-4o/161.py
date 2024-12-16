def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Test cases
assert find_lucas(9) == 76
assert find_lucas(4) == 7
assert find_lucas(3) == 4
