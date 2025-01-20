def find_aiming_point(y1, y2, yw, xb, yb, r):
    # Boundary conditions check
    if yb + r >= yw or y1 >= y2 or y1 + r >= y2 - r:
        return -1

    # Calculate the intersection point on the right wall
    # Using the geometry and reflection properties
    # The goal is to find the x_w such that the ball bounces and hits the goal
    
    # Using the fact that the reflection point must maintain the property of the line
    # We use the formula derived from the reflection geometry
    # slope = (yb - y_w) / (xb - x_w)
    # reflected_slope = (y_w - goal_y) / (x_w)
    
    # Choose a point on the goal line within the goal range
    y_goal_mid = (y1 + y2) / 2
    if y_goal_mid - r < y1 or y_goal_mid + r > y2:
        return -1

    # Calculate x_w
    x_w = xb - (2 * (yb - y_goal_mid) * (xb - 0)) / (y_goal_mid - yb)
    
    if x_w <= 0:
        return -1

    return x_w

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()

y1 = int(data[0])
y2 = int(data[1])
yw = int(data[2])
xb = int(data[3])
yb = int(data[4])
r = int(data[5])

# Calculate the result
result = find_aiming_point(y1, y2, yw, xb, yb, r)
if result == -1:
    print(result)
else:
    print(f"{result:.10f}")
