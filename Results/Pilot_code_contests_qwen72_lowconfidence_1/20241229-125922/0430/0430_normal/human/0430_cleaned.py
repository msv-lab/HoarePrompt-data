"""Reference
http://homepage1.nifty.com/gfk/circle-circle.htm
"""
(RADIUS, RADIUS_2) = (1 + 1e-12, 2 + 1e-12)
num_data = int(stdin.readline())
data = []
for _ in range(num_data):
    data.append(tuple((float(s) for s in stdin.readline().split(','))))
cross_points = []
for i in range(num_data):
    (x1, y1) = data[i]
    for j in range(num_data):
        if i == j:
            continue
        (x2, y2) = data[j]
        distance = math.hypot(x2 - x1, y2 - y1)
        if distance <= RADIUS_2:
            if x1 == x2 and y1 == y2:
                cp1 = cp2 = (x1, y1)
            else:
                th = math.atan2(y2 - y1, x2 - x1)
                al = math.acos(distance ** 2 / (2.0 * distance))
                cp1 = (x1 + math.cos(th + al), y1 + math.sin(th + al))
                cp2 = (x1 + math.cos(th - al), y1 + math.sin(th - al))
            if 0.0 <= cp1[0] <= 10.0 and 0.0 <= cp1[1] <= 10.0:
                cross_points.append(cp1)
            if 0.0 <= cp2[0] <= 10.0 and 0.0 <= cp2[1] <= 10.0:
                cross_points.append(cp2)
max_overlap = 0
for (cx, cy) in cross_points:
    count = 0
    for (x, y) in data:
        if math.hypot(cx - x, cy - y) <= RADIUS:
            count += 1
    if max_overlap < count:
        max_overlap = count
print(max_overlap)