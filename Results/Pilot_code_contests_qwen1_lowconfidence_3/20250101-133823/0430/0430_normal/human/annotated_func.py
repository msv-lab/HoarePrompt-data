#State of the program right berfore the function call: n is an integer such that 0 ≤ n ≤ 100, representing the number of stickers. Each coordinate pair xi, yi is a real number with up to 6 digits after the decimal point, and the center of each sticker is within the bounds of the 10x10 origami paper (0 ≤ xi ≤ 10 and 0 ≤ yi ≤ 10).
def func():
    """Reference
    http://homepage1.nifty.com/gfk/circle-circle.htm
    """
    RADIUS, RADIUS_2 = 1 + 1e-12, 2 + 1e-12
    num_data = int(stdin.readline())
    data = []
    for _ in range(num_data):
        data.append(tuple(float(s) for s in stdin.readline().split(',')))
        
    #State of the program after the  for loop has been executed: `RADIUS` is 1 + 1e-12, `RADIUS_2` is 2 + 1e-12, `num_data` is the number of tuples read from standard input, `data` is a list containing `num_data` tuples where each tuple contains floats.
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
        
    #State of the program after the  for loop has been executed: `RADIUS` is \(1 + 1e-12\), `RADIUS_2` is \(2 + 1e-12\), `num_data` is a positive integer, `data` is a list of tuples where each tuple contains two floats, `cross_points` is a list of all valid points that satisfy the conditions within the loop, `x1` is the first element of the `i`-th tuple in `data`, `y1` is the second element of the `i`-th tuple in `data`, `x2` is the first element of the `j`-th tuple in `data`, `y2` is the second element of the `j`-th tuple in `data`, `distance` is \( \mathit{math.hypot}(x2 - x1, y2 - y1) \), `th` is the angle calculated by \( \mathit{math.atan2}(y2 - y1, x2 - x1) \), `al` is \( \mathit{math.acos}(\frac{\mathit{distance}^2}{2.0 \times \mathit{distance}}) \), and both `cp1` and `cp2` are valid points within the range [0.0, 10.0] if they exist.
    max_overlap = 0
    for (cx, cy) in cross_points:
        count = 0
        
        for x, y in data:
            if math.hypot(cx - x, cy - y) <= RADIUS:
                count += 1
        
        if max_overlap < count:
            max_overlap = count
        
    #State of the program after the  for loop has been executed: `cross_points` is a non-empty list, `max_overlap` is the maximum count of elements in `data` for which the distance between `(cx, cy)` and `(x, y)` is less than or equal to `RADIUS`.
    print(max_overlap)
#Overall this is what the function does:The function processes a list of coordinate pairs representing the centers of circular stickers on a 10x10 origami paper. It calculates the intersection points of circles whose radii are slightly larger than 1 (to account for floating-point precision issues). For each intersection point, it counts how many original sticker centers lie within a circle of radius 1 centered at that point. Finally, it prints the maximum count of such intersections found for any point.

