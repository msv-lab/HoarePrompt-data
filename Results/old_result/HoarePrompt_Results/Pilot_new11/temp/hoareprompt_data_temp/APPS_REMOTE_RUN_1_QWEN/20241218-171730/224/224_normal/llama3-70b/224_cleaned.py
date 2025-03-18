def func_1(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

def func_2(n):
    res = 0
    for i in range(1, n + 1):
        res = max(res, func_1(res, i))
    return res

def func_3(n, f_max_n):
    MOD = 10 ** 9 + 7
    dp = [0] * (f_max_n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(f_max_n, 0, -1):
            dp[j] += dp[j - 1]
            dp[j] %= MOD
    return dp[f_max_n]
n = int(input())
f_max_n = func_2(n)
print(func_3(n, f_max_n))