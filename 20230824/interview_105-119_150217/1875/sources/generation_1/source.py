import math

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

max_area = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                area = 0.5 * abs((points[i][0] - points[k][0]) * (points[j][1] - points[l][1]) - 
                                 (points[i][1] - points[k][1]) * (points[j][0] - points[l][0]))
                max_area = max(max_area, area)

print(max_area)