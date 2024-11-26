def func_1(x):
    if x == 1:
        return [1]
    elif x == 2:
        return [3, 4]
    elif x % 2 == 1:
        return [x / 2 + 1, 2] + [1] * (x - 2)
    else:
        return [x / 2 - 1] + [1] * (x - 1)
(n, m) = map(int, raw_input().split())
for a in func_1(n):
    for b in func_1(m):
        (print(a * b),)
    print