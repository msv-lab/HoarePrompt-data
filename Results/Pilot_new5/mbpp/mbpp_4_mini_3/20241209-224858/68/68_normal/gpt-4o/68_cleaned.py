def func_1(real, imag):
    complex_number = complex(real, imag)
    return cmath.phase(complex_number)
assert math.isclose(func_1(0, 1j), 1.5707963267948966, rel_tol=0.001)
assert math.isclose(func_1(2, 1j), 0.4636476090008061, rel_tol=0.001)
assert math.isclose(func_1(0, 2j), 1.5707963267948966, rel_tol=0.001)