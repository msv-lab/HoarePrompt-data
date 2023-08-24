M, V = map(int, input().split())
lanes = []
for _ in range(M):
    D, A = map(int, input().split())
    lanes.append((D, A))

lanes.sort(reverse=True)

days = set()
for D, A in lanes:
    for i in range(1, A + 1):
        days.add(D - i + 1) 

ans = 0
for day in sorted(days):
    if V == 0:
        break
    ans += min(V, V - ans)
    V -= min(V, V - ans)

print(ans)