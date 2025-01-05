sys.setrecursionlimit(10 ** 8)

def func_1(frm, to):
    g[frm].append(to)
    rg[to].append(frm)

def func_2(now, used, back_track):
    used[now] = True
    for nx in g[now]:
        if not used[nx]:
            func_2(nx, used, back_track)
    back_track.append(now)

def func_3(now, num_cmp, used, cmp):
    used[now] = True
    cmp[now] = num_cmp
    for nx in rg[now]:
        if not used[nx]:
            func_3(nx, num_cmp, used, cmp)

def func_4(n):
    used = [False] * n
    back_track = []
    cmp = [-1] * n
    for v in xrange(n):
        if not used[v]:
            func_2(v, used, back_track)
    used = [False] * n
    num_cmp = 0
    for v in back_track[::-1]:
        if not used[v]:
            func_3(v, num_cmp, used, cmp)
            num_cmp += 1
    return (num_cmp, cmp)
(n, m) = map(int, raw_input().split())
g = [[] for _ in xrange(n)]
rg = [[] for _ in xrange(n)]
for i in xrange(m):
    (s, t) = map(int, raw_input().split())
    func_1(s, t)
(num, cmp) = func_4(n)
q = int(raw_input())
for i in xrange(q):
    (u, v) = map(int, raw_input().split())
    if cmp[u] == cmp[v]:
        print(1)
    else:
        print(0)