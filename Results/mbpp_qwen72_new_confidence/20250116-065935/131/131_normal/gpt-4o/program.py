def even_Power_Sum(n):
    return sum((2 * i) ** 5 for i in range(1, n + 1))

# Test cases
assert even_Power_Sum(2) == 1056
assert even_Power_Sum(3) == 8832
assert even_Power_Sum(1) == 32
