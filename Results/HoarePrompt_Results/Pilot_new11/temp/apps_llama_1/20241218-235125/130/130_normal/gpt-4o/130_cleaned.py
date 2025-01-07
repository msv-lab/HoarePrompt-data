input = sys.stdin.read
(N, M, K, L) = map(int, input().split())
min_x = (L + M - 1) // M
if M * min_x <= N - K:
    print(min_x)
else:
    print(-1)