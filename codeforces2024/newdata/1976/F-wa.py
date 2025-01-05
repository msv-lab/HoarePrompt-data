def count_bridges(tree):
    n = len(tree)
    dp = [[0] * (n + 1) for _ in range(n)]

    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n):
            if tree[i][j]:
                dp[i][1] += 1
                dp[i][2:] = [min(dp[i][k], dp[j][k - 1]) for k in range(2, n + 1)]

    return [min(dp[i][k] for i in range(n)) for k in range(1, n + 1)]