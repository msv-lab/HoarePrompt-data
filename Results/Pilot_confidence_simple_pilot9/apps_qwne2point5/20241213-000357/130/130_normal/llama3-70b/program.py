N, M, K, L = map(int, input().split())

if M >= N - K + 1 and M >= L:
    print(1)
else:
    print(-1)
