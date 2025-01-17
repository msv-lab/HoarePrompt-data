def find_cycle(tree, v, x):
    visited = [False] * len(tree)
    stack = [(v, None)]
    while stack:
        node, parent = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        for neighbor, weight in tree[node]:
            if neighbor == parent:
                continue
            if visited[neighbor]:
                return node, neighbor, weight ^ x
            else:
                stack.append((neighbor, node))

    return None

def solve(tree, queries):
    result = []
    for query in queries:
        if query[0] == '^':
            y = int(query[1])
            for edge in tree:
                edge[2] ^= y
        elif query[0] == '?':
            v = int(query[1])
            x = int(query[2])
            cycle = find_cycle(tree, v, x)
            if cycle:
                start, end, weight = cycle
                result.append(weight)
            else:
                result.append(-1)

    return result