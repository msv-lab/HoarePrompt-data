def func_1(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            (a[i], a[j]) = (a[j], a[i])
    (a[i + 1], a[r]) = (a[r], a[i + 1])
    return i + 1
n = int(stdin.readline())
data = [int(s) for s in stdin.readline().split()]
pat = func_1(data, 0, data[-1])
print(*data[:pat], end=' ')
print('[{}]'.format(data[pat]), *data[pat + 1:])