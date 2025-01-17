def solve():
    n, k = map(int, input().split())
    tree = {}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        if u not in tree:
            tree[u] = []
        if v not in tree:
            tree[v] = []
        tree[u].append(v)
        tree[v].append(u)
    h = int(input())
    c = 1
    p = 0
    while True:
        for u in tree[h]:
            if u != p:
                c += 1
                p = h
                h = u
                break
        if len(tree[h]) == 1:
            break
    c2 = n - c + 1
    if c2 % 2 == 0 or c % 2 == 0:
        print('Ron')
    else:
        print('Hermione')

t = 1
for _ in range(t):
    solve()
    