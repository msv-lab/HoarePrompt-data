def func_1(n):
    if n >= 5:
        return 0
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial % 10
assert func_1(4) == 4
assert func_1(21) == 0
assert func_1(30) == 0