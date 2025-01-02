#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 100. For each dataset, xi and yi are real numbers representing the coordinates of the center of the i-th sticker, with up to 6 digits after the decimal point, and all centers lie within the square origami paper with side length 10, i.e., 0 ≤ xi, yi ≤ 10. No two stickers have the same coordinates.
def func():
    """Reference
    http://homepage1.nifty.com/gfk/circle-circle.htm
    """
    RADIUS, RADIUS_2 = 1 + 1e-12, 2 + 1e-12
    num_data = int(stdin.readline())
    data = []
    for _ in range(num_data):
        data.append(tuple(float(s) for s in stdin.readline().split(',')))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer such that 0 ≤ n ≤ 100, `xi` and `yi` are real numbers representing the coordinates of the center of the i-th sticker, with up to 6 digits after the decimal point, and all centers lie within the square origami paper with side length 10, i.e., 0 ≤ `xi`, `yi` ≤ 10, no two stickers have the same coordinates, `RADIUS` is `1.000000000001`, `RADIUS_2` is `2.000000000001`, `num_data` is a non-negative integer, `data` is a list containing `num_data` tuples of floats read from standard input.
    cross_points = []
    for i in range(num_data):
        x1, y1 = data[i]
        
        for j in range(num_data):
            if i == j:
                continue
            x2, y2 = data[j]
            distance = math.hypot(x2 - x1, y2 - y1)
            if distance <= RADIUS_2:
                if x1 == x2 and y1 == y2:
                    cp1 = cp2 = x1, y1
                else:
                    th = math.atan2(y2 - y1, x2 - x1)
                    al = math.acos(distance ** 2 / (2.0 * distance))
                    cp1 = x1 + math.cos(th + al), y1 + math.sin(th + al)
                    cp2 = x1 + math.cos(th - al), y1 + math.sin(th - al)
                if 0.0 <= cp1[0] <= 10.0 and 0.0 <= cp1[1] <= 10.0:
                    cross_points.append(cp1)
                if 0.0 <= cp2[0] <= 10.0 and 0.0 <= cp2[1] <= 10.0:
                    cross_points.append(cp2)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer such that \(0 \leq n \leq 100\), `xi` and `yi` are real numbers representing the coordinates of the center of the i-th sticker, with up to 6 digits after the decimal point, and all centers lie within the square origami paper with side length 10, i.e., \(0 \leq xi, yi \leq 10\), no two stickers have the same coordinates, `RADIUS` is \(1.000000000001\), `RADIUS_2` is \(2.000000000001\), `num_data` is a non-negative integer, `data` is a list containing `num_data` tuples of floats read from standard input, `cross_points` is a list containing all valid intersection points between circles centered at points in `data` with radius `RADIUS_2` and circles centered at other points in `data` with the same radius, where each intersection point lies within the bounds of the square origami paper. If `num_data` is 0, `cross_points` remains an empty list.
    max_overlap = 0
    for (cx, cy) in cross_points:
        count = 0
        
        for x, y in data:
            if math.hypot(cx - x, cy - y) <= RADIUS:
                count += 1
        
        if max_overlap < count:
            max_overlap = count
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer such that \(0 \leq n \leq 100\), `xi` and `yi` are real numbers representing the coordinates of the center of the i-th sticker, with up to 6 digits after the decimal point, and all centers lie within the square origami paper with side length 10, i.e., \(0 \leq xi, yi \leq 10\), no two stickers have the same coordinates, `RADIUS` is \(1.000000000001\), `RADIUS_2` is \(2.000000000001\), `num_data` is a non-negative integer, `data` is a list containing `num_data` tuples of floats read from standard input, `cross_points` is a list containing all valid intersection points between circles centered at points in `data` with radius `RADIUS_2` and circles centered at other points in `data` with the same radius, where each intersection point lies within the bounds of the square origami paper. `max_overlap` is the maximum number of points in `data` that lie within a distance `RADIUS` from any point in `cross_points`. If `cross_points` is empty (which implies `num_data` is 0 or the circles do not intersect within the bounds), `max_overlap` remains 0.
    print(max_overlap)
#Overall this is what the function does:The function reads a series of coordinates from the standard input, representing the centers of circular stickers placed on a square origami paper with side length 10. It calculates the maximum number of stickers that can overlap at any single point on the paper, considering the intersection points of circles with a slightly larger radius (approximately 2 units). The function then prints this maximum overlap count. If no intersections occur or if no data is provided, the function prints 0. Edge cases include scenarios where no stickers are provided (`num_data` is 0) or where the circles do not intersect within the bounds of the paper. The function ensures that all coordinates are within the specified range and that no two stickers share the same coordinates.

