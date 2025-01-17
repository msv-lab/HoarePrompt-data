def get_max_sum(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n < 12:
        return n
    
    # Recursively calculate the value for f(n)
    max_sum = max(
        get_max_sum(n // 2, memo) +
        get_max_sum(n // 3, memo) +
        get_max_sum(n // 4, memo) +
        get_max_sum(n // 5, memo),
        n
    )
    
    memo[n] = max_sum
    return max_sum

# Test cases
assert get_max_sum(60) == 106
assert get_max_sum(10) == 12
assert get_max_sum(2) == 2
