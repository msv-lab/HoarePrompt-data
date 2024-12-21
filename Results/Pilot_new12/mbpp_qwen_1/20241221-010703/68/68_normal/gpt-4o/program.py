import cmath

def angle_complex(real, imag):
    # Create the complex number
    complex_number = complex(real, imag)
    # Return the phase (angle) of the complex number
    return cmath.phase(complex_number)

# Test cases
import math

assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
assert math.isclose(angle_complex(2,1j), 0.4636476090008061, rel_tol=0.001)
assert math.isclose(angle_complex(0,2j), 1.5707963267948966, rel_tol=0.001)
