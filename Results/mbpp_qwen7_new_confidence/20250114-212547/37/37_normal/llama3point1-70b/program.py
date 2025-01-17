import math

def volume_sphere(radius: float) -> float:
    """
    Calculate the volume of a sphere.

    Args:
    radius (float): The radius of the sphere.

    Returns:
    float: The volume of the sphere.
    """
    return (4/3) * math.pi * (radius ** 3)
