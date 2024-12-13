import cmath

def angle_complex(real, imag):
    complex_num = complex(real, imag)
    return cmath.phase(complex_num)
