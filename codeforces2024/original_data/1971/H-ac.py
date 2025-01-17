def is_solvable(field):
    n = len(field[0])
    graph = [[] for i in range(2 * n + 1)]
    for a, b, c in zip(*field):
        graph[-a].extend((b, c))
        graph[-b].extend((a, c))
        graph[-c].extend((a, b))
    status = [0] * len(graph)
    def try_fill(i):
        traversal = [i]
        status[i] = 1
        status[-i] = -1
        processed = 0
        while processed < len(traversal):
            v = traversal[processed]
            processed += 1
            for u in graph[v]:
                if status[u] == -1:
                    for w in traversal:
                        status[w] = 0
                        status[-w] = 0
                    return False
                if status[u] == 0:
                    status[u] = 1
                    status[-u] = -1
                    traversal.append(u)
        return True
    
    for i in range(1, n + 1):
        if status[i] != 0:
            continue
        if not (try_fill(i) or try_fill(-i)):
            return "NO"
    return "YES"
    
n_tests = int(input())
for test_id in range(n_tests):
    n = int(input())
    field = []
    for i in range(3):
        field.append(list(map(int, input().split())))
    print(is_solvable(field))