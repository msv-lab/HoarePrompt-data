#State of the program right berfore the function call: a and b are non-negative integers such that a > 0 and b >= 0.
def func_1(a, b):
    """Compute the Greatest Common Divisor (GCD) of a and b using the Extended Euclidean Algorithm."""
    if (a == 0) :
        return b, 0, 1
        #The program returns b with its original value, 0, and 1
    #State of the program after the if block has been executed: a is a non-negative integer greater than 0, b is a non-negative integer, the GCD of a and b is computed using the Extended Euclidean Algorithm, a is not equal to 0
    gcd_val, x1, y1 = func_1(b % a, a)
    x = y1 - b // a * x1
    y = x1
    return gcd_val, x, y
    #The program returns gcd_val which is the greatest common divisor of `a` and `b`, x which is `y1 - b // a * x1`, and y which is `x1`
#Overall this is what the function does:The function `func_1` accepts two non-negative integers `a` and `b` where `a` > 0. It returns either the original value of `b` along with 0 and 1, or the greatest common divisor (gcd) of `a` and `b`, and the coefficients `x` and `y` such that `ax + by = gcd(a, b)`. If `a` is 0, the function returns `b`, 0, and 1 directly. Otherwise, it recursively computes the gcd and the coefficients using the Extended Euclidean Algorithm. The final state of the program is that it provides the gcd of `a` and `b`, and the Bézout coefficients `x` and `y` that satisfy the equation `ax + by = gcd(a, b)` unless `a` is 0, in which case it simply returns `b`, 0, and 1.

