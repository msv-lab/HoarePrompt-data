def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def expected_length(m):
    MOD = 10**9 + 7
    res = 0
    for i in range(1, m + 1):
        res += pow(i, MOD - 2, MOD)
    return res

m = int(input())
print(expected_length(m))
