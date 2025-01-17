n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

lines = {}
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        if x1 == x2:
            slope = 'inf'
        else:
            slope = (y2 - y1) * 1.0 / (x2 - x1)
        if slope not in lines:
            lines[slope] = set()
        lines[slope].add((x1, y1))
        lines[slope].add((x2, y2))

for slope, pts in lines.items():
    if len(pts) == n:
        print("YES")
        exit()

print("NO")
