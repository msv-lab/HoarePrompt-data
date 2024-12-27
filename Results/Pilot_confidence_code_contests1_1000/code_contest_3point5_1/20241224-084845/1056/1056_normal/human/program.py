import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def par(a):
    if P[a] < 0: return a
    t = par(P[a])
    P[a] = t
    return t
def unite(a, b):
    if par(a) == par(b): return 0
    C[par(a)], C[par(b)] = C[par(a)] + C[par(b)], C[par(a)] + C[par(b)]
    if P[par(b)] == P[par(a)]:
        P[par(b)] = par(a)
        P[par(a)] -= 1
    elif P[par(b)] > P[par(a)]:
        P[par(b)] = par(a)
    else:
        P[par(a)] = par(b)
N, H, W = map(int, input().split())
P = [-1 for i in range(H+W)]
C = [1] * (H+W)
X = []
for _ in range(N):
    r, c, a = map(int, input().split())
    X.append((a, r-1, c+H-1))
X = sorted(X)
ans = 0
while X:
    a, r, c = X.pop()
    unite(r, c)
    if C[par(r)]:
        ans += a
        C[par(r)] -= 1
print(ans)