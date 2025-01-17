def test_three_equal(a, b, c):
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0

# Tests
assert test_three_equal(1, 1, 1) == 3
assert test_three_equal(-1, -2, -3) == 0
assert test_three_equal(1, 2, 2) == 2
