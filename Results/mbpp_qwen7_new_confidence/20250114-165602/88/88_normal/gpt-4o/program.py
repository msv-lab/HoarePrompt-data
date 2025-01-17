def sum_series(n):
    total_sum = 0
    for i in range(n // 2 + 1):
        term = n - 2 * i
        if term > 0:
            total_sum += term
    return total_sum

# Test cases to validate the solution
assert sum_series(0) == 0
assert sum_series(6) == 12
assert sum_series(10) == 30
assert sum_series(9) == 25
