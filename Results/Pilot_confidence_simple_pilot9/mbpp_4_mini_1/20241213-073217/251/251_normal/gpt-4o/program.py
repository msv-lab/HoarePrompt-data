import math

def polar_rect(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return (r, theta)

# Test cases
assert polar_rect(3, 4) == (5.0, 0.9272952180016122)
assert polar_rect(4, 7) == (8.06225774829855, 1.0516502125483738)
assert polar_rect(15, 17) == (22.67156809750927, 0.8478169733934057)
