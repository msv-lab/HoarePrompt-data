import math

def lateralsuface_cylinder(radius, height):
    return 2 * math.pi * radius * height

# Test cases
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
assert math.isclose(lateralsuface_cylinder(4,5), 125.66000000000001, rel_tol=0.001)
assert math.isclose(lateralsuface_cylinder(4,10), 251.32000000000002, rel_tol=0.001)
