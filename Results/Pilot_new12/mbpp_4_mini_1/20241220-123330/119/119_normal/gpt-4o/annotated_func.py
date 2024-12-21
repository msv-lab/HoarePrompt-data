#State of the program right berfore the function call: a and b are numbers (can be integers or floats).
def func_1(a, b):
    return b, a
    #The program returns the values of b and a, where b is a number and a is a number
#Overall this is what the function does:The function accepts two parameters, `a` and `b`, which can be either integers or floats. It returns a tuple containing the values of `b` and `a`, in that order. The function does not perform any additional validation or manipulation of the input parameters, meaning it behaves the same regardless of the types or values of `a` and `b`, including edge cases such as empty values, None, or non-numeric types. The final state of the program is that a tuple with the values `(b, a)` is returned.

