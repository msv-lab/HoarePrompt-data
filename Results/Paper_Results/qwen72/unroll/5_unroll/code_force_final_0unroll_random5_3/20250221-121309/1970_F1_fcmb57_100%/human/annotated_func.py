#State of the program right berfore the function call: a and b are integers representing the dimensions of the Quidditch field, such that 3 <= a, b <= 99 and both a and b are odd.
def func_1(a, b):
    x, y = a
    dx, dy = b
    return x + dx, y + dy
    #The program returns the new coordinates (x + dx, y + dy), where `x` and `y` are the original coordinates, and `dx` and `dy` are the changes in the x and y directions, respectively.
#Overall this is what the function does:The function `func_1` accepts two parameters, `a` and `b`. It is intended to unpack `a` into `x` and `y`, and `b` into `dx` and `dy`. However, the function will raise a `ValueError` if `a` or `b` cannot be unpacked into two values. If the unpacking is successful, the function returns a tuple `(x + dx, y + dy)`, which represents the new coordinates after applying the changes `dx` and `dy` to the original coordinates `x` and `y`.

