#State of the program right berfore the function call: a and b are integers such that a >= 0 and b >= 0.
def func_1(a, b):
    """Compute the Greatest Common Divisor (GCD) of a and b using the Extended Euclidean Algorithm."""
    if (a == 0) :
        return b, 0, 1
        #The program returns b with its original value (an integer such that b >= 0), 0, and 1
    #State of the program after the if block has been executed: a and b are integers such that a >= 0 and b >= 0; a is not equal to 0
    gcd_val, x1, y1 = func_1(b % a, a)
    x = y1 - b // a * x1
    y = x1
    return gcd_val, x, y
    #`gcd_val`, which is the GCD of `a` and `b`, `x`, which is `y1 - b // a * x1`, and `y`, which is `y1`
#Overall this is what the function does:- The function correctly handles the case where `a` is zero, returning `b`, 0, and 1.
- For all other cases, the function correctly applies the Extended Euclidean Algorithm to compute the GCD and related coefficients.

