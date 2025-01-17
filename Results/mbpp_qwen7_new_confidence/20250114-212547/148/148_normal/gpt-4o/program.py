import math

def otherside_rightangle(a, b):
    return math.sqrt(a**2 + b**2)

# Test cases
assert math.isclose(otherside_rightangle(7, 8), 10.63014581273465, rel_tol=0.001)
assert math.isclose(otherside_rightangle(3, 4), 5, rel_tol=0.001)
assert math.isclose(otherside_rightangle(7, 15), 16.55294535724685, rel_tol=0.001)
