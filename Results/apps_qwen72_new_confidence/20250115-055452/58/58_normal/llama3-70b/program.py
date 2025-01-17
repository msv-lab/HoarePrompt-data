n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

def find_area(points):
    x_coords = sorted(list(set([point[0] for point in points])))
    y_coords = sorted(list(set([point[1] for point in points])))
    if len(x_coords) != 2 or len(y_coords) != 2:
        return -1
    else:
        return abs((x_coords[1] - x_coords[0]) * (y_coords[1] - y_coords[0]))

print(find_area(points))
