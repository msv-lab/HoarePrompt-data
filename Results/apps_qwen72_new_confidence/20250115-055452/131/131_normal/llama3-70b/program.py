n, m = map(int, input().split())
paper = [list(input()) for _ in range(n)]

black_cells = [(i, j) for i in range(n) for j in range(m) if paper[i][j] == 'B']

if not black_cells:
    print(1)
else:
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
    for x, y in black_cells:
        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)

    side = max_x - min_x + 1
    if side != max_y - min_y + 1:
        print(-1)
    else:
        print(side * side - len(black_cells))
