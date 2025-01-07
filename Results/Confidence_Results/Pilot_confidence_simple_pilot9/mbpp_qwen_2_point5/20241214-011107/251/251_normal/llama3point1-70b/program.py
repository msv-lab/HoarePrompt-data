import math

def polar_rect(x, y):
    r = math.hypot(x, y)
    phi = math.atan2(y, x)
    return (r, phi)
