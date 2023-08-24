def inverse_mod(q, MOD):
    return pow(q, MOD-2, MOD)

def solve(n, m, MOD):
    MULTIPLIER = 2  # The number of cards in the current deck doubles after a joker is drawn
    DECK_SIZE = n + m
    expected_time = 0
    
    # Calculate (n + m)!
    factorial = 1
    for i in range(1, DECK_SIZE + 1):
        factorial = (factorial * i) % MOD
    
    # Calculate (n + m - i)!, where i = 0, 1, 2, ..., n - 1
    factorials = [0] * n
    factorials[0] = factorial
    for i in range(1, n):
        factorials[i] = (factorials[i - 1] * inverse_mod(DECK_SIZE - i, MOD)) % MOD
    
    # Calculate the expected time
    for i in range(n):
        expected_time = (expected_time + MULTIPLIER * factorials[i]) % MOD
        MULTIPLIER = (MULTIPLIER * 2) % MOD
    
    return expected_time

n, m = map(int, input().split())
MOD = 998244353
result = solve(n, m, MOD)
print(result)