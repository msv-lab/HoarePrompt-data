sys.setrecursionlimit(1 << 29)

def func_1():
    return [int(x) for x in stdin.readline().split()]

def func_2():
    return int(stdin.readline())

def func_3():
    return stdin.readline().strip()
N = func_2()
op = [0] + func_1()
pa = [0, 0] + func_1()
G = defaultdict(list)
for i in range(2, N + 1):
    p = pa[i]
    G[p].append(i)
nleaf = [0] * (N + 1)
for i in range(N, 0, -1):
    if len(G[i]) == 0:
        nleaf[i] = 1
        continue
    for j in G[i]:
        nleaf[i] += nleaf[j]
memo = {}

def func_4(root):
    global memo
    if len(G[root]) == 0:
        return 1
    if root in memo:
        return memo[root]
    res = 0
    if op[root] == 0:
        for v in G[root]:
            res = max(res, func_4(v))
    else:
        nl = nleaf[root]
        for v in G[root]:
            nlv = nleaf[v]
            res = max(res, nl - (nlv - func_4(v)))
    memo[root] = res
    return memo[root]
for i in range(N, 0, -1):
    func_4(i)
res = func_4(1)
print(res)