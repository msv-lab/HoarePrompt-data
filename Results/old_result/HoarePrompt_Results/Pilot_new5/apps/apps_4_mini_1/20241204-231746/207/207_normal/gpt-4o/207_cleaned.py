def func_1(x, y):
    while y:
        (x, y) = (y, x % y)
    return x

def func_2(m, a, b):
    g = func_1(a, b)
    if g != 1:
        return func_2(m // g, a // g, b // g) * g
    k = a + b - 1
    if m < k:
        return (m + 1) * (m + 2) // 2
    sum_k = k * (k + 1) // 2
    sum_m = m * (m + 1) // 2 - k * (k - 1) // 2
    return sum_k + sum_m
(m, a, b) = map(int, input().split())
result = func_2(m, a, b)
print(result)