def func_1(n):
    directions = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
    (x, y) = (0, 0)
    steps = 1
    direction_index = 0
    while n > 0:
        for _ in range(2):
            if n >= steps:
                (dx, dy) = directions[direction_index]
                x += dx * steps
                y += dy * steps
                n -= steps
                direction_index = (direction_index + 1) % 6
            else:
                (dx, dy) = directions[direction_index]
                x += dx * n
                y += dy * n
                return (x, y)
        steps += 1
    return (x, y)
n = int(input().strip())
(x, y) = func_1(n)
print(x, y)