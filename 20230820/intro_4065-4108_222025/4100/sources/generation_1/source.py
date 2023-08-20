N, K, Q = map(int, input().split())
scores = [K] * N

for i in range(Q):
    ans = int(input())
    for j in range(N):
        if j != ans - 1:
            scores[j] -= 1

for score in scores:
    if score > 0:
        print("Yes")
    else:
        print("No")