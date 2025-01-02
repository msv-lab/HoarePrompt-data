def func_1(n, k, edges):
    storage = [-1] * (4 * n)
    storage_index = 0
    lookup = [-1] * (n + 1)
    for (u, v) in edges:
        storage[storage_index] = lookup[u]
        storage[storage_index + 1] = v
        lookup[u] = storage_index
        storage_index += 2
        storage[storage_index] = lookup[v]
        storage[storage_index + 1] = u
        lookup[v] = storage_index
        storage_index += 2
    nodes = [0] * (2 * (n + 1))
    stack = [n]
    stack_pop = stack.pop
    stack_append = stack.append
    while stack:
        index = stack_pop()
        parent_index = nodes[index * 2]
        t = lookup[index]
        while t >= 0:
            v = storage[t + 1]
            t = storage[t]
            if v == parent_index:
                continue
            nodes[v * 2] = index
            stack_append(v)
    count = n - k
    for i in xrange(n, 0, -1):
        new_nodes = []
        p = i * 2
        abort = False
        while True:
            flag = nodes[p + 1]
            if flag == -1:
                abort = True
                break
            elif flag == 1:
                break
            new_nodes.append(p)
            index = nodes[p]
            if index <= 0:
                break
            p = index * 2
        if abort:
            for p in new_nodes:
                nodes[p + 1] = -1
            continue
        c = count - len(new_nodes)
        if c >= 0:
            for p in new_nodes:
                nodes[p + 1] = 1
            count = c
            if count == 0:
                break
        else:
            for j in xrange(-c):
                nodes[new_nodes[j] + 1] = -1
    result = [i for i in xrange(1, n + 1) if nodes[i * 2 + 1] != 1]
    print(' '.join(map(str, result)))

def func_2():
    sys.setcheckinterval(2147483647)
    (n, k) = map(int, sys.stdin.readline().split())
    edges = [map(int, sys.stdin.readline().split()) for _ in xrange(n - 1)]
    func_1(n, k, edges)
if __name__ == '__main__':
    func_2()