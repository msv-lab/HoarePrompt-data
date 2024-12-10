#State of the program right berfore the function call: real and imag are numbers (integers or floats).
def func_1(real, imag):
    complex_number = complex(real, imag)
    return cmath.phase(complex_number)
    #The program returns the phase of the complex number represented by complex(real, imag)
#Overall this is what the function does:The function accepts two parameters, `real` and `imag`, which can be either integers or floats. It creates a complex number from these parameters and returns the phase (angle) of that complex number in radians.

