def func_1(N):
    return [{} for _ in range(N)]
assert func_1(5) == [{}, {}, {}, {}, {}]
assert func_1(6) == [{}, {}, {}, {}, {}, {}]
assert func_1(7) == [{}, {}, {}, {}, {}, {}, {}]