def func_1(n, m, screen):
    top = bottom = left = right = None
    for i in range(n):
        for j in range(m):
            if screen[i][j] == 'w':
                if top is None:
                    top = bottom = i
                    left = right = j
                else:
                    if i < top:
                        top = i
                    if i > bottom:
                        bottom = i
                    if j < left:
                        left = j
                    if j > right:
                        right = j
    if top is None or bottom is None or left is None or (right is None):
        return -1
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if frame_height < 2 or frame_width < 2:
        return -1
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or (j == right):
                if result[i][j] == '.':
                    result[i][j] = '+'
    return result
(n, m) = map(int, input().split())
screen = [input().strip() for _ in range(n)]
result = func_1(n, m, screen)
if result == -1:
    print(-1)
else:
    for row in result:
        print(''.join(row))