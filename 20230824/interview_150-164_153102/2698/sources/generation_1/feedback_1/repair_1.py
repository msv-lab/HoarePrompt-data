M, V = map(int, input().split())
lanes = []
for _ in range(M):
    D, A = map(int, input().split())
    lanes.append((D, A))

# Sorting the lanes in descending order is not required

days = set()
for D, A in lanes:
    for i in range(D - A + 1, D + 1):
        days.add(i)

ans = 0
for day in sorted(days):
    if V == 0:
        break
    ans += min(V, len(days) - ans)  # Fixing the calculation of the number of vegetables collected
    V -= min(V, len(days) - ans)  # Fixing the decrement of the daily capacity

print(len(days))  # Fixing the printing of the final answer