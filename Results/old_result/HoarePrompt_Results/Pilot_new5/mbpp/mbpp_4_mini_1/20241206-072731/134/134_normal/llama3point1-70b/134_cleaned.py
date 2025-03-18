def func_1(n):
    sum = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum += math.comb(n, i)
    return sum