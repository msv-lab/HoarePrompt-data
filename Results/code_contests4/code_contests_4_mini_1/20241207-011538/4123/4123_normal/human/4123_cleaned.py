(n, x1, y1, x2, y2) = map(int, raw_input().split())

def func_1(x, y):
    if y == 0:
        return x
    if x == n:
        return y + n
    if y == n:
        return n - x + n + n
    return n - y + n + n + n
print(func_1(x2, y2) - func_1(x1, y1) + 4 * n) % (4 * n)