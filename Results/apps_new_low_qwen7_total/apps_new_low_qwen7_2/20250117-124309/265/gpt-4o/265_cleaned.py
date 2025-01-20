MOD = 10 ** 9 + 7

def func_1(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i % MOD
    return result

def func_2(n, m):
    fact_n = func_1(n)
    fact_n_m = func_1(n - m)
    ways = pow(2, m, MOD) * fact_n % MOD * pow(fact_n_m, MOD - 2, MOD) % MOD
    return ways
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
m = int(data[1])
result = func_2(n, m)
print(result)