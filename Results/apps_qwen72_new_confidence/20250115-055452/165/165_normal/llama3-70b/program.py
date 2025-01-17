def calculate_xw(y1, y2, y_w, x_b, y_b, r):
    # Calculate the slope of the line from the ball to the goal
    m = (y2 - y1) / (0 - x_b)
    
    # Calculate the y-intercept of the line from the ball to the goal
    b = y_b - m * x_b
    
    # Calculate the x-coordinate of the point where the ball hits the wall
    x_w = (y_w - b) / m
    
    # Check if the ball hits the wall and bounces into the goal
    if x_w > x_b and y_w - r <= m * x_w + b <= y_w + r:
        return x_w
    else:
        return -1

y1, y2, y_w, x_b, y_b, r = map(int, input().split())
x_w = calculate_xw(y1, y2, y_w, x_b, y_b, r)
print('{:.8f}'.format(x_w) if x_w != -1 else '-1')
