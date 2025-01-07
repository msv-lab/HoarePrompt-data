#State of the program right berfore the function call: real and imag are floating-point numbers representing the real and imaginary parts of a complex number, respectively.
def func_1(real, imag):
    complex_num = complex(real, imag)
    return cmath.phase(complex_num)
    #The program returns the phase angle (in radians) of the complex number with real part `real` and imaginary part `imag`
#Overall this is what the function does:The function accepts two floating-point numbers `real` and `imag`, creates a complex number from these parts, and returns the phase angle (in radians) of this complex number.

