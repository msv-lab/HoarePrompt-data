import math

def volume_cylinder(radius, height):
    # Calculate the volume using the formula for the volume of a cylinder
    volume = math.pi * (radius ** 2) * height
    return volume

# Tests to validate the function
assert math.isclose(volume_cylinder(10, 5), 1570.7500000000002, rel_tol=0.001)
assert math.isclose(volume_cylinder(4, 5), 251.32000000000002, rel_tol=0.001)
assert math.isclose(volume_cylinder(4, 10), 502.64000000000004, rel_tol=0.001)
