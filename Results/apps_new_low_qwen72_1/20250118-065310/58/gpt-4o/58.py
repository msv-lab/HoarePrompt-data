def determine_area(n, vertices):
    if n == 1 or n == 3:
        return -1
    elif n == 2:
        x1, y1 = vertices[0]
        x2, y2 = vertices[1]
        return abs(x2 - x1) * abs(y2 - y1)
    else:  # n == 4
        x_coords = set()
        y_coords = set()
        for x, y in vertices:
            x_coords.add(x)
            y_coords.add(y)
        if len(x_coords) == 2 and len(y_coords) == 2:
            return abs(max(x_coords) - min(x_coords)) * abs(max(y_coords) - min(y_coords))
        else:
            return -1

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    vertices = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        vertices.append((x, y))
        index += 2
    print(determine_area(n, vertices))
