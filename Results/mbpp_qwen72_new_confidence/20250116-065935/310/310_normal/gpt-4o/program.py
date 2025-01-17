import math

def area_tetrahedron(edge_length):
    return math.sqrt(3) * edge_length ** 2

# Tests
assert math.isclose(area_tetrahedron(3), 15.588457268119894, rel_tol=0.001)
assert math.isclose(area_tetrahedron(20), 692.8203230275509, rel_tol=0.001)
assert math.isclose(area_tetrahedron(10), 173.20508075688772, rel_tol=0.001)
