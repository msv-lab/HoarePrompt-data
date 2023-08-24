x1, y1, x2, y2 = map(int, input().split())

# Calculate the difference between x1 and x2, y1 and y2 to get the distance
dx = x1 - x2
dy = y1 - y2

# Restore x3 and y3 by subtracting dy from x2 and adding dx to y2
x3 = x2 - dy
y3 = y2 + dx

# Restore x4 and y4 by subtracting dx from x3 and subtracting dy from y3
x4 = x3 - dx
y4 = y3 - dy

print(x3, y3, x4, y4)