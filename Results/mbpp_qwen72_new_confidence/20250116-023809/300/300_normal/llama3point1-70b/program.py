import math

def lateralsurface_cone(r, h):
    l = math.sqrt(r**2 + h**2)
    return math.pi * r * l