N, K, Q = map(int, input().split())
players = [K] * N

for _ in range(Q):
    A = int(input())
    players[A-1] -= 1

for i in range(N):
    if players[i] <= 0:
        print("No")
    else:
        print("Yes")