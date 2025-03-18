def func_1(n, k):
    multiplier = 10 ** k
    x = n * (multiplier // math.gcd(n, multiplier))
    return x
(n, k) = map(int, input().split())
print(func_1(n, k))