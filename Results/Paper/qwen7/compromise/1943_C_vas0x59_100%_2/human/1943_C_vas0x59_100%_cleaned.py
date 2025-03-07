def func_1(l):
    return max(range(len(l)), key=lambda x: l[x])

def func_2():
    n = int(input())
    u2vs = [[] for _ in range(n)]
    for _ in range(n - 1):
        (u, v) = tuple(map(int, input().split()))
        u -= 1
        v -= 1
        u2vs[u].append(v)
        u2vs[v].append(u)

    def bfs(s):
        nonlocal n
        d = [-1 for _ in range(n)]
        prev = [-1 for _ in range(n)]
        q = [s]
        d[s] = 0
        while len(q) > 0:
            u = q.pop(0)
            du = d[u]
            for v in u2vs[u]:
                if d[v] == -1:
                    d[v] = du + 1
                    prev[v] = u
                    q.append(v)
        return (d, prev)
    (d, _) = bfs(0)
    a = func_1(d)
    (d, previous) = bfs(a)
    b = func_1(d)
    path_ba = [b]
    while True:
        n = previous[path_ba[-1]]
        if n == -1:
            break
        path_ba.append(n)
    ops = []
    if len(path_ba) % 2 == 1:
        ci = len(path_ba) // 2
        c = path_ba[ci]
        for i in range(ci + 1):
            ops.append((c, i))
    else:
        ci2 = len(path_ba) // 2
        ci1 = ci2 - 1
        c1 = path_ba[ci1]
        c2 = path_ba[ci2]
        for i in range(1, len(path_ba) - ci1, 2):
            ops.append((c1, i))
            ops.append((c2, i))
    print(len(ops))
    print(*map(lambda x: f'{x[0] + 1} {x[1]}', ops), sep='\n')
    return None
if __name__ == '__main__':
    for _ in range(int(input())):
        func_2()