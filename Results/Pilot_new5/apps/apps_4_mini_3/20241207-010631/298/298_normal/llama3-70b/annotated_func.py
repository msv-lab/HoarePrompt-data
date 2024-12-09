#State of the program right berfore the function call: a and b are integers, where a >= 0 and b >= 0.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the GCD of the original values of `a` and `b`. If the original value of `b` was 0, then `a` is unchanged.
    return a
    #The program returns the value of 'a', which is the GCD of the original values of 'a' and 'b', and since 'b' is 0, 'a' remains unchanged
#Overall this is what the function does:The function accepts two non-negative integers `a` and `b`, and calculates the greatest common divisor (GCD) of these two numbers. If `b` is initially 0, the function returns `a` unchanged. The function handles cases where both `a` and `b` are zero, in which case it returns 0 as the GCD of two zeros.

#State of the program right berfore the function call: a and b are integers, where b is a non-negative integer.
def func_2(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns the values 1 and 0
    else :
        x, y = func_2(b, a % b)
        return y, x - a // b * y
        #The program returns y and x - a // b * y, where y and x are assigned the values returned by func_2(b, a % b), with b being a non-negative integer greater than 0.
#Overall this is what the function does:The function accepts two parameters, `a` (an integer) and `b` (a non-negative integer). It implements the Extended Euclidean Algorithm, which returns a tuple. If `b` is 0, it returns (1, 0). Otherwise, it recursively computes the values based on the inputs, ultimately returning (y, x - a // b * y), where `x` and `y` are derived from the recursive call with parameters (b, a % b). This means the function calculates coefficients x and y such that `a*x + b*y = gcd(a, b)`.

#State of the program right berfore the function call: a and b are integers representing dimensions related to the problem, where the output of func_2(a, b) returns a tuple (x, y) with non-negative integers and x * a + y * b is an integer.
def func_3(a, b):
    x, y = func_2(a, b)
    return x, y, x * a + y * b
    #The program returns the values of x and y, as well as the result of the expression x * a + y * b, where x and y are non-negative integers obtained from the function func_2(a, b) and x * a + y * b is an integer.
#Overall this is what the function does:The function `func_3` accepts two integer parameters `a` and `b`, calls another function `func_2(a, b)` to obtain non-negative integers `x` and `y`, and returns a tuple containing `x`, `y`, and the result of the expression `x * a + y * b`. The values of `x` and `y` are guaranteed to be non-negative integers, and `x * a + y * b` will be an integer as a result of the multiplication and addition operations.

