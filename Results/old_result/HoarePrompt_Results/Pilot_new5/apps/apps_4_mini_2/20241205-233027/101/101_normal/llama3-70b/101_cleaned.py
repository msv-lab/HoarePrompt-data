(n, m) = map(int, input().split())
pixels = [list(input()) for _ in range(n)]
white_pixels = [(i, j) for i in range(n) for j in range(m) if pixels[i][j] == 'w']
(min_x, min_y, max_x, max_y) = (float('inf'), float('inf'), float('-inf'), float('-inf'))
for (x, y) in white_pixels:
    (min_x, min_y) = (min(min_x, x), min(min_y, y))
    (max_x, max_y) = (max(max_x, x), max(max_y, y))
frame_size = max(max_x - min_x, max_y - min_y) + 1
if frame_size > max(n, m):
    print(-1)
else:
    for i in range(n):
        for j in range(m):
            if (i == min_x or i == max_x or j == min_y or (j == max_y)) and pixels[i][j] == '.':
                pixels[i][j] = '+'
            elif pixels[i][j] == 'w':
                continue
            else:
                pixels[i][j] = '.'
    for row in pixels:
        print(''.join(row))