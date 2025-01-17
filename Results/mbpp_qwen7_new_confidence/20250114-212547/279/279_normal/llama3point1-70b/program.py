import math

def triangle_area(radius):
    if radius < 0:
        return None
    if radius == 0:
        return 0
    area = (radius ** 2) * math.pi / 2
    return area
