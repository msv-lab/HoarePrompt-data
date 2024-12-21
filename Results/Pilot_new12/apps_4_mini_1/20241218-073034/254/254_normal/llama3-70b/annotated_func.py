#State of the program right berfore the function call: a, b, and c are integers representing the time intervals of the garlands, where 1 ≤ a, b, c ≤ 1500.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the GCD of the original values of `a` and `b`, `c` remains unchanged.
    return a
    #The program returns the GCD of the original values of 'a' and 'b', where 'b' is 0 and 'a' is unchanged
#Overall this is what the function does:The function accepts two integer parameters, `a` and `b`, which represent time intervals of garlands. It calculates and returns the greatest common divisor (GCD) of the original values of `a` and `b`. After the function execution, `b` becomes 0, while the value of `a` is replaced with the computed GCD. The function does not modify or use a third parameter, `c`, which remains unchanged throughout. The function handles all inputs where 1 ≤ a, b ≤ 1500 and assumes both inputs are positive integers. If either input is zero (though the specification states 1 ≤ a, b), the GCD logic will yield results consistent with mathematical definitions.

