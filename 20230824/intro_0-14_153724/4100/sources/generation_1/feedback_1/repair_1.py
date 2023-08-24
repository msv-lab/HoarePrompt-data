N, K, Q = map(int, input().split())
scores = [K] * N

for _ in range(Q):
    A = int(input())
    
    # Subtract 1 from scores of other players
    for i in range(N):
        if i+1 != A:
            scores[i] -= 1

for score in scores:
    if score >= 0:  # Check for surviving players
        print("Yes")
    else:
        print("No")