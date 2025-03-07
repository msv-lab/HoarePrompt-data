def func_1(nodes, start, parent=None):
    if len(nodes[start]) == 1 and nodes[start][0] == parent:
        return False
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.append(not func_1(nodes, node, start))
    return any(distances)

def func_2():
    (n, t) = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        (u, v) = map(int, input().split())
        nodes[u].append(v)
        nodes[v].append(u)
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
    start = int(input())
    moves = func_1(nodes, start)
    if moves:
        print('Ron')
    else:
        print('Hermione')
t = 1
for i in range(t):
    func_2()