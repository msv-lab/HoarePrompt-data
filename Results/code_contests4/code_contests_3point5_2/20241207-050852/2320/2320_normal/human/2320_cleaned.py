def func_1(a, b):
    if b == 0:
        return (a, 1, 0)
    (g, tmp_x, tmp_y) = func_1(b, a % b)
    x = tmp_y
    y = tmp_x - tmp_y * (a / b)
    return (g, x, y)
(n, m, dx, dy) = map(int, raw_input().split())
count = [0] * n
for i in range(0, m):
    (x, y) = map(int, raw_input().split())
    (g, t, k) = func_1(n, dy)
    k = -k * y
    rep_x = ((x + k * dx) % n + n) % n
    count[rep_x] = count[rep_x] + 1
ans_x = 0
for x in range(0, n):
    if count[x] > count[ans_x]:
        ans_x = x
print(ans_x, 0)