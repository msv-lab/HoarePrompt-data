def square_Sum(n):
    return sum((2 * i) ** 2 for i in range(1, n + 1))

# Test cases
assert square_Sum(2) == 20
assert square_Sum(3) == 56
assert square_Sum(4) == 120
