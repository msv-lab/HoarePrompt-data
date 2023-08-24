N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

max_score = float('-inf')

for i in range(N):
    curr_score = 0
    visited = set()
    j = i
    while j not in visited:
        curr_score += C[j]
        visited.add(j)
        j = P[j] - 1
        max_score = max(max_score, curr_score)
        # Stop iterating if the maximum possible score has been reached
        if curr_score >= K:
            break

print(max_score)