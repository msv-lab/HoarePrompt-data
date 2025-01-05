import math

def circle_from_points(x1, y1, x2, y2):
    # Center of the circle
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    
    # Radius of the circle
    r = math.sqrt((x1 - cx)**2 + (y1 - cy)**2)
    
    return (cx, cy, r)

def circle_from_three_points(x1, y1, x2, y2, x3, y3):
    # Slopes of the lines formed by the points
    m1 = (y2 - y1) / (x2 - x1) if x1 != x2 else float('inf')
    m2 = (y3 - y2) / (x3 - x2) if x2 != x3 else float('inf')
    
    # Center of the circle
    cx = (m1*m2*(y1 - y3) + m2*(x1 + x2) - m1*(x2 + x3)) / (2 * (m2 - m1))
    cy = (-1/m1) * (cx - (x1 + x2) / 2) + (y1 + y2) / 2 if m1 != 0 else (-1/m2) * (cx - (x2 + x3) / 2) + (y2 + y3) / 2
    
    # Radius of the circle
    r = math.sqrt((x1 - cx)**2 + (y1 - cy)**2)
    
    return (cx, cy, r)

def smallest_enclosing_circle(points):
    n = len(points)
    circle = None
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, r1 = points[i]
            x2, y2, r2 = points[j]
            
            # Circles from two points
            circle = circle_from_points(x1, y1, x2, y2)
            
            # Check if the circle contains all points
            valid = True
            for k in range(n):
                x, y, r = points[k]
                if (x - circle[0])**2 + (y - circle[1])**2 > (r + circle[2])**2:
                    valid = False
                    break
            
            if valid:
                return circle
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x1, y1, r1 = points[i]
                x2, y2, r2 = points[j]
                x3, y3, r3 = points[k]
                
                # Circle from three points
                circle = circle_from_three_points(x1, y1, x2, y2, x3, y3)
                
                # Check if the circle contains all points
                valid = True
                for l in range(n):
                    x, y, r = points[l]
                    if (x - circle[0])**2 + (y - circle[1])**2 > (r + circle[2])**2:
                        valid = False
                        break
                
                if valid:
                    return circle

# Read the number of circles
n = int(input().strip())

# Read the circles
circles = []
for _ in range(n):
    x, y, r = map(int, input().strip().split())
    circles.append((x, y, r))

# Find the smallest enclosing circle
result = smallest_enclosing_circle(circles)

# Output the result
print("{:.10f} {:.10f} {:.10f}".format(result[0], result[1], result[2]))