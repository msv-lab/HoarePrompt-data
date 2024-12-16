#State of the program right berfore the function call: a, b, and the third input integer (not shown in the provided function definition but mentioned in the problem description) are integers such that 1 ≤ k_i ≤ 1500 for i in {1, 2, 3}.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `a` is the greatest common divisor (GCD) of the original values of `a` and `b`, `b` is 0
    return a
    #The program returns `a`, which is the greatest common divisor of the original values of `a` and `b`, and `b` is 0
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`, and returns the greatest common divisor (GCD) of `a` and `b`.

