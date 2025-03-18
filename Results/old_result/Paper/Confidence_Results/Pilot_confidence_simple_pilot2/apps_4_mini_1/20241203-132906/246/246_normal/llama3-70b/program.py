n = int(input())
rectangles = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append((x1, y1, x2, y2))

min_x = min(x1 for x1, _, _, _ in rectangles)
max_x = max(x2 for _, _, _, x2 in rectangles)
min_y = min(y1 for _, _, _, y2 in rectangles)
max_y = max(y2 for _, _, _, _ in rectangles)

square_size = max_x - min_x
if max_y - min_y != square_size:
    print("NO")
else:
    points = set()
    for x1, y1, x2, y2 in rectangles:
        for x in range(x1, x2):
            for y in range(y1, y2):
                points.add((x, y))
    if len(points) == square_size ** 2:
        print("YES")
    else:
        print("NO")
