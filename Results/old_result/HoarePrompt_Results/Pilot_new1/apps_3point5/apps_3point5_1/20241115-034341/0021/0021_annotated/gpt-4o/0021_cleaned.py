n = int(input())
a = list(map(int, input().split()))
min_pos = a.index(1)
max_pos = a.index(n)
dist1 = abs(0 - max_pos)
dist2 = abs(n - 1 - max_pos)
dist3 = abs(0 - min_pos)
dist4 = abs(n - 1 - min_pos)
max_distance = max(dist1, dist2, dist3, dist4)
print(max_distance)