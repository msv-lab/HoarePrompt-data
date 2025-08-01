import cmath

def convert(num):
    return cmath.polar(complex(num))

# Test cases
assert convert(1) == (1.0, 0.0)
assert convert(4) == (4.0, 0.0)
assert convert(5) == (5.0, 0.0)
