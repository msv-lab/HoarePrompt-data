def func_1(n):
    if n == 0 or n == 1:
        return 1
    (S0, S1) = (1, 1)
    for i in range(2, n + 1):
        S_next = 2 * S1 + S0
        (S0, S1) = (S1, S_next)
    return S1
assert func_1(3) == 7
assert func_1(4) == 17
assert func_1(5) == 41