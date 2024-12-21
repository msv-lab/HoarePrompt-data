#State of the program right berfore the function call: a and b are positive integers where \(1 \leq a, b \leq 10^9\).
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `a` is equal to the greatest common divisor (GCD) of `a_original` and `b_original`; `b` is 0
    return a
    #The program returns `a`, which is equal to the greatest common divisor (GCD) of `a_original` and `b_original`
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `a` and `b` where \(1 \leq a, b \leq 10^9\). It computes the greatest common divisor (GCD) of `a` and `b` using the Euclidean algorithm. After the loop has been executed, `a` will hold the GCD of the original values of `a` and `b`, and `b` will be 0. The function returns `a`.

#State of the program right berfore the function call: a and b are non-negative integers where \(b \neq 0\), and they represent the divisor and remainder in the Euclidean algorithm respectively.
def func_2(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns 1 and 0
    else :
        x, y = func_2(b, a % b)
        return y, x - a // b * y
        #`The program returns y, x - a // b * y` where `x` and `y` are the return values of `func_2(b, a % b)`
#Overall this is what the function does:The function `func_2` accepts two non-negative integers `a` and `b` (with \(b \neq 0\)) and implements a recursive version of the Extended Euclidean Algorithm. If `b` is zero, the function returns `(1, 0)`. Otherwise, it recursively calls itself with parameters `b` and `a % b`, and returns the values `y` and `x - a // b * y`, where `x` and `y` are the results of the recursive call. This process continues until `b` becomes zero.

#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func_3(a, b):
    x, y = func_2(a, b)
    return x, y, x * a + y * b
    #`The program returns x, y, and x * a + y * b`, where `x` and `y` are returned by `func_2(a, b)`
#Overall this is what the function does:The function `func_3` accepts two positive integer parameters `a` and `b` (1 ≤ a, b ≤ 10^9). It calls another function `func_2(a, b)` which returns two values `x` and `y`. Then, `func_3` computes the value of `x * a + y * b` and returns three values: `x`, `y`, and `x * a + y * b`. The function ensures that `x` and `y` are valid outputs from `func_2(a, b)` and returns them along with their linear combination with `a` and `b`.

