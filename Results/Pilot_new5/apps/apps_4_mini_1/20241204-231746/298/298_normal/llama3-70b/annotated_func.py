#State of the program right berfore the function call: a and b are integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `a` is the greatest common divisor of the original values of `a` and `b`, `b` is 0.
    return a
    #The program returns the greatest common divisor of the original values of `a` and `b`, where `b` is 0, which means the returned value is `a`.
#Overall this is what the function does:The function accepts two integers `a` and `b`, and returns their greatest common divisor (GCD), returning `a` if `b` is zero at the start.

#State of the program right berfore the function call: a and b are integers, where b is not equal to zero.
def func_2(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns 1 and 0
    else :
        x, y = func_2(b, a % b)
        return y, x - a // b * y
        #The program returns a tuple consisting of y and the result of x minus the integer division of a by b multiplied by y, where a and b are integers and b is not equal to zero
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`, where `b` is guaranteed to be non-zero. It uses a recursive approach to calculate and return a tuple consisting of two values: one being the result of the extended Euclidean algorithm. The first value of the tuple is derived from the recursive call, while the second value is computed as `x - (a // b) * y`. If `b` is zero in a hypothetical scenario (though the code ensures this won't happen), it would return (1, 0).

#State of the program right berfore the function call: a and b are integers representing two of the input values from the problem description (n, m, and k), with 1 ≤ a, b ≤ 10^9 and 2 ≤ k ≤ 10^9.
def func_3(a, b):
    x, y = func_2(a, b)
    return x, y, x * a + y * b
    #The program returns the values of x and y, which are the results of func_2(a, b), and the result of the expression x * a + y * b, where x and y depend on the specific implementation of func_2 with inputs a and b.
#Overall this is what the function does:The function accepts two integer parameters, `a` and `b`, calls another function `func_2` with these parameters to obtain values `x` and `y`, and returns a tuple containing `x`, `y`, and the computed value of the expression `x * a + y * b`. The actual results of `x` and `y` depend on the implementation of `func_2`.

