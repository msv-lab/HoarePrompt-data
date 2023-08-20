N, K, Q = map(int, input().split())
scores = [K] * N

for i in range(Q):
    ans = int(input())
    scores[ans - 1] += 1

for score in scores:
    if score - Q > 0:
        print("Yes")
    else:
        print("No")