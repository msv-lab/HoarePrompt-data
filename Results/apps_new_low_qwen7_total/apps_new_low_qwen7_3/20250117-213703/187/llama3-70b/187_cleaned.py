(n, m) = map(int, input().split())
towers = set()
for i in range(1, n + 1):
    towers.add(i * 2)
for i in range(1, m + 1):
    towers.add(i * 3)
print(max(towers))