# Read input
x1, y1, x2, y2 = map(int, input().split())

# Check if the given points form a vertical or horizontal line
if x1 == x2:
    side_length = abs(y2 - y1)
    x3, y3 = x1 + side_length, y1
    x4, y4 = x2 + side_length, y2
    print(x3, y3, x4, y4)
elif y1 == y2:
    side_length = abs(x2 - x1)
    x3, y3 = x1, y1 + side_length
    x4, y4 = x2, y2 + side_length
    print(x3, y3, x4, y4)
# Check if the given points are diagonally opposite on a square
elif abs(x2 - x1) == abs(y2 - y1):
    x3, y3 = x1, y2
    x4, y4 = x2, y1
    print(x3, y3, x4, y4)
else:
    print(-1)
