def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def f_max(n):
    res = 0
    for i in range(1, n+1):
        res = max(res, gcd(res, i))
    return res

def count_permutations(n, f_max_n):
    MOD = 10**9 + 7
    dp = [0]*(f_max_n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(f_max_n, 0, -1):
            dp[j] += dp[j-1]
            dp[j] %= MOD
    return dp[f_max_n]

n = int(input())
f_max_n = f_max(n)
print(count_permutations(n, f_max_n))
