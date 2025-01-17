def can_cross_bridge(N, M, weights, bridge):
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(M):
            if dp[i][j]:
                if j < M and weights[i] <= bridge[j][1]:
                    dp[i + 1][j + 1] = True
                dp[i + 1][j] = True
    return dp[N][M]

def main():
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    bridge = [list(map(int, input().split())) for _ in range(M)]
    weights.sort()
    bridge.sort(key=lambda x: x[0])
    l, r = 0, 10**18
    while l < r:
        mid = (l + r) // 2
        if can_cross_bridge(N, M, weights, [(l, v) for l, v in bridge]):
            r = mid
        else:
            l = mid + 1
    if l == 10**18:
        print(-1)
    else:
        print(l)

if __name__ == "__main__":
    main()
