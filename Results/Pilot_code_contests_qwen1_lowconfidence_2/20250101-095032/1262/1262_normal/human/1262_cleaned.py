N = input()
V = list(map(int, input().split()))
M = 1000000000.0
for i in range(1, len(V)):
    diff = abs(sum(V[:i]) - sum(V[i:]))
    if M > diff:
        M = diff
print(M)