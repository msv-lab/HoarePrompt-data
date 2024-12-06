def func_1(n):
    k = 1
    while True:
        triangular_number = k * (k + 1) // 2
        if len(str(triangular_number)) == n:
            return k
        k += 1
assert func_1(2) == 4
assert func_1(3) == 14
assert func_1(4) == 45