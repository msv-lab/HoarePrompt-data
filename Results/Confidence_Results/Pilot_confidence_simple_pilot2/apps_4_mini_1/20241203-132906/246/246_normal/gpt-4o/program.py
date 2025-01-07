# Use Standard Input format
import sys
input = sys.stdin.read

# Reading input
data = input().split()
n = int(data[0])
rectangles = []
index = 1
for _ in range(n):
    x1 = int(data[index])
    y1 = int(data[index+1])
    x2 = int(data[index+2])
    y2 = int(data[index+3])
    rectangles.append((x1, y1, x2, y2))
    index += 4

# Determine the bounding box
min_x = min(rect[0] for rect in rectangles)
min_y = min(rect[1] for rect in rectangles)
max_x = max(rect[2] for rect in rectangles)
max_y = max(rect[3] for rect in rectangles)

# Calculate the area of the bounding box
bounding_box_area = (max_x - min_x) * (max_y - min_y)

# Check if bounding box is a square
is_square = (max_x - min_x) == (max_y - min_y)

# Calculate the sum of the areas of the rectangles
total_area = sum((rect[2] - rect[0]) * (rect[3] - rect[1]) for rect in rectangles)

# Determine if the rectangles form a square
if is_square and total_area == bounding_box_area:
    print("YES")
else:
    print("NO")
