def func_1():
    return sys.stdin.readline().split()
dom = []
n = int(func_1()[0])
for i in range(n):
    dom.append(func_1())
    dom[i].append(i)
    for j in range(len(dom[i])):
        dom[i][j] = int(dom[i][j])
dom.sort()
seg = 4 * n * [0]
res = n * [0]
inf = 1000 * 1000 * 100 + 10

def func_2(i, val, s, e, x):
    seg[x] = max(seg[x], val)
    if e - s < 2:
        return
    m = (e + s) / 2
    if i < m:
        func_2(i, val, s, m, 2 * x)
    else:
        func_2(i, val, m, e, 2 * x + 1)

def func_3(x, s, e, l, r):
    print('infind %d %d-%d %d-%d' % (x, s, e, l, r))
    if s >= r or e <= l:
        return 0
    print('passed')
    if s == l and e == r or e - s < 2:
        print('wtf? %d' % seg[x])
        return seg[x]
    m = (e + s) / 2
    return max(func_3(2 * x, s, m, l, min(r, m)), func_3(2 * x + 1, m, e, max(m, l), r))

def func_4(i):
    [x, h] = dom[i][0:2]
    s = i
    e = n
    while e - s > 1:
        m = int((e + s) / 2)
        print('bs %d' % m)
        if dom[m][0] < x + h:
            s = m
        else:
            e = m
    print('find %d %d - %d %d' % (i, e, x, h))
    return func_3(1, 0, n, i, e)
indx = n
while indx > 0:
    indx -= 1
    res[indx] = [dom[indx][2], max(indx + 1, func_4(indx)), indx]
    print('res %d: %d' % (indx, res[indx][1]))
    func_2(indx, res[indx][1], 0, n, 1)
    log = ''
    for x in seg:
        log += str(x) + ' '
    print(log)
print(res)
res.sort()
out = ''
for i in range(n):
    out += str(res[i][1] - res[i][2]) + ' '
print(out)