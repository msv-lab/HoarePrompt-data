N, K, Q = map(int, input().split())
scores = [K] * N

for _ in range(Q):
    A = int(input())
    scores[A-1] -= 1

for score in scores:
    if score > 0:
        print("Yes")
    else:
        print("No")