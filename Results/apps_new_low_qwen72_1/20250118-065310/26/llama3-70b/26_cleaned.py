(n, k) = map(int, input().split())
if k > n * (n + 1) // 2:
    print(-1)
    exit()
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1):
        if k > 0:
            matrix[i][j] = 1
            matrix[j][i] = 1
            k -= 1
for row in matrix:
    print(' '.join(map(str, row)))