def power(a, n, p):
    res = 1
    while n > 0:
        if n & 1:
            res = (res * a) % p
        a = (a * a) % p
        n = n // 2
    return res

def count_functions(p, k):
    if k == 0:
        return power(p, p - 1, 1000000007)
    else:
        return power(p, p, 1000000007)

p, k = map(int, input().split())
num_functions = count_functions(p, k)
print(num_functions)