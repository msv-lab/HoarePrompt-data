def func_1():
    (n, t) = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        (u, v) = map(int, input().split())
        nodes[u].append(v)
        nodes[v].append(u)
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
    (s, e) = list(ends)
    tree = [s]
    prev = s
    curr = nodes[s][0]
    while curr != e:
        tree.append(curr)
        if nodes[curr][0] == prev:
            prev = curr
            curr = nodes[curr][1]
        else:
            prev = curr
            curr = nodes[curr][0]
    tree.append(e)
    start = int(input())
    idx = tree.index(start)
    moves = [idx, n - idx - 1]
    if any([move % 2 == 1 for move in moves]):
        print('Ron')
    else:
        print('Hermione')
t = 1
for i in range(t):
    func_1()