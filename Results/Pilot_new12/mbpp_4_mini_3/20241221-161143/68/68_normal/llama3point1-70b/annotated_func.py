#State of the program right berfore the function call: real and imag are floating-point numbers representing the real and imaginary parts of a complex number, respectively.
def func_1(real, imag):
    complex_num = complex(real, imag)
    return cmath.phase(complex_num)
    #The program returns the phase of the complex number represented as complex(real, imag)
#Overall this is what the function does:The function `func_1` accepts two parameters, `real` and `imag`, both of which are floating-point numbers representing the real and imaginary parts of a complex number, respectively. It creates a complex number from these inputs and returns the phase (or angle) of that complex number in radians. The function handles cases where either or both parts of the complex number are zero, as well as any other real or imaginary values. There are no safeguards or error handling for non-numeric inputs, so it assumes valid floating-point numbers are provided. After execution, the program outputs the angle of the complex number based on its input components.

