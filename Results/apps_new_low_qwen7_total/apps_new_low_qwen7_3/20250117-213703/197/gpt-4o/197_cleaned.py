MOD = 10 ** 9 + 7

def func_1(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base % mod
        base = base * base % mod
        exponent //= 2
    return result

def func_2(x, k):
    if x == 0:
        return 0
    power = func_1(2, k + 1, MOD)
    result = x * (power - 1) % MOD % MOD
    return result
input = sys.stdin.read
(x, k) = map(int, input().split())
print(func_2(x, k))