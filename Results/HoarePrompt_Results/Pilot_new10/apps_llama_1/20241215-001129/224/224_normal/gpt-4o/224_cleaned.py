MOD = 10 ** 9 + 7

def func_1(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = result * i % mod
    return result
n = int(input())
if n == 2:
    result = 1
else:
    result = func_1(n - 1, MOD)
print(result)