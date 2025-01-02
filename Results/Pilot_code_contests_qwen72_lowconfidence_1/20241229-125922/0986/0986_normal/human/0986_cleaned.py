(N, M) = map(int, raw_input().split())
es = [[] for i in range(N)]
for i in range(M):
    (a, b) = map(int, raw_input().split())
    (a, b) = (a - 1, b - 1)
    es[a].append(b)
    es[b].append(a)
colors = [0 for i in range(N)]

def func_1(v, color):
    colors[v] = color
    for to in es[v]:
        if colors[to] == color:
            return False
        if colors[to] == 0 and (not func_1(to, -color)):
            return False
    return True

def func_2():
    return func_1(0, 1)
if func_2():
    b = (sum(colors) + N) // 2
    w = N - b
    print(b * w - M)
else:
    all = N * (N - 1) // 2
    print(all - M)