#State of the program right berfore the function call: a and b are integers such that a ≠ b and 1 ≤ a, b ≤ 10^6.
def func_1(a, b):
    return a if b == 0 else func_1(b, a % b)
    #The program returns the value of 'a' if 'b' is 0; otherwise, it recursively calls func_1 with 'b' and 'a' modulo 'b', continuing until 'b' becomes 0, ultimately returning the non-zero value of 'a' or 'b' at that point.
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`, and recursively computes the greatest common divisor (GCD) of `a` and `b` using the Euclidean algorithm. It returns `a` if `b` is 0; otherwise, it continues calling itself with `b` and `a % b` until `b` becomes 0, ultimately returning the GCD of the original values of `a` and `b`. The function assumes that `a` and `b` are non-zero integers, as specified in the precondition.

