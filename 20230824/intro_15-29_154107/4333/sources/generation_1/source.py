x1, y1, x2, y2 = map(int, input().split())

#calculate the difference between x1 and x2, y1 and y2 to get the distance
dx = x2 - x1
dy = y2 - y1

#restore x3 and y3 by adding dy to x2 and subtracting dx to y2
x3 = x2 + dy
y3 = y2 - dx

#restore x4 and y4 by adding dx to x3 and dy to y3
x4 = x3 + dx
y4 = y3 + dy

print(x3, y3, x4, y4)