def bfs(graph, start):
    queue = [(start, 1)]
    visited = set()
    visited.add(start)

    while queue:
        node, time = queue.pop(0)
        row, col = node

        if graph[row][col] == 'D' and col != 0:
            return time

        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < len(graph) and 0 <= c < len(graph[0]) and (r, c) not in visited and graph[r][c] not in ['X', '*']:
                visited.add((r, c))
                queue.append(((r, c), time+1))
                if graph[r][c] == '.':
                    graph[r][c] = '*'

    return -1

R, C = map(int, input().strip().split())
graph = []
start = None
for _ in range(R):
    row = list(input().strip())
    if 'S' in row:
        start = (_, row.index('S'))
    graph.append(row)

time_needed = bfs(graph, start)
if time_needed == -1:
    print("KAKTUS")
else:
    print(time_needed)