#State of the program right berfore the function call: **
def func_1(a, b):
    if (b == 0) :
        return a, 1, 0
        #The program returns the integer value of `a`, the integer value of 1, and the integer value of 0. The value of `b` is equal to 0.
    #State of the program after the if block has been executed: `b` is a variable, and its value is not equal to 0.
    g, tmp_x, tmp_y = func_1(b, a % b)
    x = tmp_y
    y = tmp_x - tmp_y * (a / b)
    return g, x, y
    #The program returns the values of 'g', 'x', and 'y'. The value of 'g' is the result of calling 'func_1'. The value of 'x' is the new value of 'tmp_y'. The value of 'y' is calculated based on the new values of 'tmp_x', 'tmp_y', 'a', and 'b'.
#Overall this is what the function does:The function `func_1` accepts two integer parameters, `a` and `b`, and performs the Euclidean Algorithm to calculate the greatest common divisor (gcd) of `a` and `b`. 
If `b` is 0, it returns the integer value of `a`, 1, and 0. 
In other cases, it recursively calls itself with `b` and `a % b`, then calculates and returns the gcd as 'g', along with new values for 'x' and 'y' based on the recursive calls. 
The functionality of the function is to compute the gcd of two integers using the Euclidean Algorithm.

