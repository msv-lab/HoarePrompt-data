import cmath
def convert(n):
    complex_num = complex(n)
    polar_coordinates = cmath.polar(complex_num)
    return polar_coordinates
