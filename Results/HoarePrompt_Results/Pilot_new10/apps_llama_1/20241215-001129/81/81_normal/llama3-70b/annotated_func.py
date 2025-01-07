#State of the program right berfore the function call: a and b are integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the greatest common divisor of the original `a` and `b`
    return a
    #The program returns the greatest common divisor of the original `a` and 0, which is essentially the absolute value of `a`, but since `a` is already defined in this context as its own GCD with 0, it returns `a`.
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`, and returns their greatest common divisor

#State of the program right berfore the function call: a and b are positive integers.
def func_2(a, b):
    return a * b // func_1(a, b)
    #The program returns the integer result of the product of positive integers `a` and `b` divided by the result of `func_1(a, b)`
#Overall this is what the function does:The function accepts two positive integers `a` and `b`, calculates their product, and attempts to divide it by the result of `func_1(a, b)`. If `func_1(a, b)` returns a non-zero value, it returns the integer result of this division; otherwise, it raises a `ZeroDivisionError`.

