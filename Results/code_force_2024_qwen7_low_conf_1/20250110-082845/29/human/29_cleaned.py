def func_1(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

def func_2(n, m):
    count = 0
    for a in range(1, n + 1):
        for b in range(1, m + 1):
            if (a + b) % (b * func_1(a, b)) == 0:
                count += 1
    return count