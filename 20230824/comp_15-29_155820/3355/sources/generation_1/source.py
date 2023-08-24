import itertools

# Read input
n, T = map(int, input().split())
tasks = []
for _ in range(n):
    p, t, d = map(int, input().split())
    tasks.append((p, t, d))
times = [list(map(int, input().split())) for _ in range(n + 2)]

# Calculate the maximum points using dynamic programming
dp = [[0] * (T + 1) for _ in range(n + 2)]
prev = [[-1] * (T + 1) for _ in range(n + 2)]
for i in range(1, n + 1):
    for j in range(T + 1):
        if tasks[i - 1][2] != -1 and tasks[i - 1][2] < j:
            continue
        dp[i][j] = dp[i - 1][j]
        prev[i][j] = j
        for k in range(n + 2):
            if k != i:
                if tasks[i - 1][2] != -1 and j + times[k][i] <= T and dp[i - 1][j + times[k][i]] + tasks[i - 1][0] > dp[i][j]:
                    dp[i][j] = dp[i - 1][j + times[k][i]] + tasks[i - 1][0]
                    prev[i][j] = k

# Find the path from the ending location to the starting location
path = []
j = T
for i in range(n, 0, -1):
    if prev[i][j] == -1:
        break
    path.append(i)
    j = prev[i][j]
path.reverse()

# Print the maximum points and the indices of the tasks
print(dp[n][0])
if dp[n][0] > 0:
    print(' '.join(map(str, path)))
else:
    print('')