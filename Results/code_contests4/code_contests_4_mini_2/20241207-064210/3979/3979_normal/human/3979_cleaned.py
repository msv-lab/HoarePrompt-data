(a, b, x1, y1, x2, y2) = map(int, raw_input().split())

def func_1(c, d):
    if c >= 0:
        return c / d
    return c / d
aa = func_1(x1 + y1, 2 * a)
aaa = func_1(x2 + y2, 2 * a)
ans1 = abs(aaa - aa)
bb = func_1(x1 - y1, 2 * b)
bbb = func_1(x2 - y2, 2 * b)
ans2 = abs(bbb - bb)
print(max(ans1, ans2))