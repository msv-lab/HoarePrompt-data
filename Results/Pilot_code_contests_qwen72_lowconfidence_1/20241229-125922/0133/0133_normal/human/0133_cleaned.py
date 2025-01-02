"""
NTC here
"""
inp = sys.stdin.readline

def func_1():
    return inp().strip()
out = []

def func_2():
    return int(func_1())

def func_3():
    return list(map(int, func_1().split()))
range = xrange
input = raw_input
INF = 10 ** 5 + 7
n = func_2()
adj = [[] for i in range(n + 1)]
for _ in range(n - 1):
    (i, j) = func_3()
    adj[i].append(j)
    adj[j].append(i)

def func_4(adj, start=1):
    n = len(adj)
    visited = [False] * n
    first = [-1] * n
    euler = []
    height = [-1] * n
    srt = [start]
    height[start] = 1
    parent = [-1] * n
    while srt:
        v = srt.pop()
        if visited[v]:
            euler.append(v)
            continue
        first[v] = len(euler)
        euler.append(v)
        visited[v] = True
        if parent[v] != -1:
            srt.append(parent[v])
        for u in adj[v]:
            if not visited[u]:
                parent[u] = v
                height[u] = height[v] + 1
                srt.append(u)
    return (first, euler, height)
(first, euler, height) = func_4(adj)
euler = [height[i] for i in euler]

class RangeQuery:

    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        (i, n) = (1, len(_data[0]))
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, begin, end):
        end += 1
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin], self._data[depth][end - (1 << depth)])
sa = RangeQuery(euler)

def func_5(i, j):
    (l, r) = (first[i], first[j])
    if l > r:
        (l, r) = (r, l)
    h = sa.query(l, r)
    return height[i] + height[j] - 2 * h
q = func_2()
while q:
    q -= 1
    (x, y, a, b, k) = func_3()
    ans1 = [func_5(a, b), func_5(a, x) + 1 + func_5(y, b), func_5(a, y) + 1 + func_5(x, b)]
    for i in ans1:
        if k - i >= 0 and (k - i) % 2 == 0:
            out.append('YES')
            break
    else:
        out.append('NO')
print('\n'.join(out))