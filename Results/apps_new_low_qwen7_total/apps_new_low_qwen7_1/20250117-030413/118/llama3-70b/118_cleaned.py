(N, M) = map(int, input().split())
north_south_lines = []
for _ in range(N):
    (A, B, C) = map(int, input().split())
    north_south_lines.append((C, A, B))
east_west_lines = []
for _ in range(M):
    (D, E, F) = map(int, input().split())
    east_west_lines.append((D, E, F))

def func_1(line1, line2):
    (x1, y1, x2) = line1
    (x3, y3, x4) = line2
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return False
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom
    if 0 <= t <= 1 and 0 <= u <= 1:
        return True
    return False
north_south_lines.sort(key=cmp_to_key(lambda x, y: x - y))
east_west_lines.sort(key=cmp_to_key(lambda x, y: x - y))
x_points = set()
y_points = set()
for i in range(N):
    for j in range(i + 1, N):
        if north_south_lines[i][0] == north_south_lines[j][0]:
            continue
        x_points.add(north_south_lines[i][0])
        x_points.add(north_south_lines[j][0])
for i in range(M):
    for j in range(i + 1, M):
        if east_west_lines[i][0] == east_west_lines[j][0]:
            continue
        y_points.add(east_west_lines[i][0])
for i in range(N):
    for j in range(M):
        if func_1(north_south_lines[i], east_west_lines[j]):
            x_points.add(north_south_lines[i][0])
            y_points.add(east_west_lines[j][0])
x_points = sorted(list(x_points))
y_points = sorted(list(y_points))
area = 0
for i in range(len(x_points) - 1):
    for j in range(len(y_points) - 1):
        area += (x_points[i + 1] - x_points[i]) * (y_points[j + 1] - y_points[j])
if area == 0:
    print('INF')
else:
    print(area)