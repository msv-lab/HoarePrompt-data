N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dist = [[float('inf')] * (N * N + 1) for _ in range(3)]
parent = [[None] * (N * N + 1) for _ in range(3)]
for i in range(3):
    dist[i][1] = 0
    queue = deque([(1, i)])
    while queue:
        (cur, piece) = queue.popleft()
        for x in range(N):
            for y in range(N):
                if A[x][y] == cur:
                    for (dx, dy) in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
                        (nx, ny) = (x + dx, y + dy)
                        if 0 <= nx < N and 0 <= ny < N:
                            ncur = A[nx][ny]
                            if piece == 0 and dist[0][ncur] > dist[0][cur] + 1:
                                dist[0][ncur] = dist[0][cur] + 1
                                parent[0][ncur] = (cur, piece)
                                queue.append((ncur, 0))
                    for (dx, dy) in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        (nx, ny) = (x + dx, y + dy)
                        if 0 <= nx < N and 0 <= ny < N:
                            ncur = A[nx][ny]
                            if piece == 1 and dist[1][ncur] > dist[1][cur] + 1:
                                dist[1][ncur] = dist[1][cur] + 1
                                parent[1][ncur] = (cur, piece)
                                queue.append((ncur, 1))
                    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        (nx, ny) = (x + dx, y + dy)
                        if 0 <= nx < N and 0 <= ny < N:
                            ncur = A[nx][ny]
                            if piece == 2 and dist[2][ncur] > dist[2][cur] + 1:
                                dist[2][ncur] = dist[2][cur] + 1
                                parent[2][ncur] = (cur, piece)
                                queue.append((ncur, 2))
                    if piece != i:
                        queue.append((cur, i))
ans = float('inf')
ans_replace = float('inf')
for i in range(3):
    if dist[i][N * N] < ans:
        ans = dist[i][N * N]
        ans_replace = 0
    elif dist[i][N * N] == ans:
        replace = 0
        cur = N * N
        while cur != 1:
            (cur, piece) = parent[i][cur]
            if piece != i:
                replace += 1
        if replace < ans_replace:
            ans_replace = replace
print(ans, ans_replace)