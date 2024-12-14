def find_frame(n, m, screen):
    top = bottom = left = right = None

    # Find the bounding box of white pixels
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

    if top is None or bottom is None or left is None or right is None:
        return -1

    # Check if the bounding box can form a frame
    frame_height = bottom - top + 1
    frame_width = right - left + 1
    if frame_height < 2 or frame_width < 2:
        return -1

    # Create the result screen with the frame
    result = [list(row) for row in screen]
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if i == top or i == bottom or j == left or j == right:
                if result[i][j] == '.':
                    result[i][j] = '+'

    return result

# Read input
n, m = map(int, input().split())
screen = [input().strip() for _ in range(n)]

# Find the frame
result = find_frame(n, m, screen)

# Print the result
if result == -1:
    print(-1)
else:
    for row in result:
        print(''.join(row))
