def test_three_equal(a, b, c):
    counts = [a, b, c].count(a)
    if counts == 1:
        return 0
    else:
        return counts
