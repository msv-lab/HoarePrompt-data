import math

n = int(input())
vectors = []
for _ in range(n):
    x, y = map(int, input().split())
    vectors.append((x, y))

min_angle = float('inf')
ans = (-1, -1)
for i in range(n):
    for j in range(i + 1, n):
        xi, yi = vectors[i]
        xj, yj = vectors[j]
        dot_product = xi * xj + yi * yj
        magnitude_i = math.sqrt(xi ** 2 + yi ** 2)
        magnitude_j = math.sqrt(xj ** 2 + yj ** 2)
        angle = math.acos(dot_product / (magnitude_i * magnitude_j))
        if angle < min_angle:
            min_angle = angle
            ans = (i + 1, j + 1)

print(*ans)
