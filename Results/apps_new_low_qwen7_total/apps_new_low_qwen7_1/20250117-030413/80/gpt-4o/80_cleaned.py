MOD = 10 ** 9 + 7

def func_1(a, p):
    return pow(a, p - 2, p)

def func_2(m):
    if m == 1:
        return 1
    length_sum = 0
    for i in range(1, m + 1):
        length_sum += func_1(i, MOD)
        length_sum %= MOD
    result = m * length_sum % MOD
    return result
m = int(input().strip())
print(func_2(m))