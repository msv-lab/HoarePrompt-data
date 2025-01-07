#State of the program right berfore the function call: a and b are positive integers where \(1 \le a, b \le 10^9\).
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `a` is the greatest common divisor (GCD) of the original values of `a` and `b`; `b` is 0.
    return a
    #The program returns `a`, which is the greatest common divisor (GCD) of the original values of `a` and `b`
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` where \(1 \le a, b \le 10^9\) and returns their greatest common divisor (GCD). The function uses the Euclidean algorithm to iteratively reduce the problem until `b` becomes 0, at which point `a` contains the GCD of the original values of `a` and `b`.

#State of the program right berfore the function call: a and b are positive integers where \(1 \le a, b \le 10^9\) and \(b \neq 0\).
def func_2(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns 1 and 0
    else :
        x, y = func_2(b, a % b)
        return y, x - a // b * y
        #`y, y - a // b * y`
#Overall this is what the function does:The function `func_2` accepts two positive integers `a` and `b` and returns a tuple `(x, y)` where `ax + by = gcd(a, b)`. If `b` is zero, it returns `(1, 0)`.

#State of the program right berfore the function call: a and b are positive integers such that \(1 \le a, b \le 10^9\).
def func_3(a, b):
    x, y = func_2(a, b)
    return x, y, x * a + y * b
    #The program returns x, y, and x*a + y*b, where x and y are the return values of func_2(a, b)
#Overall this is what the function does:The function `func_3` accepts two positive integers `a` and `b` (where \(1 \le a, b \le 10^9\)). It calls another function `func_2(a, b)` which returns two values `x` and `y`. The function then returns these two values along with their linear combination `x*a + y*b`.

