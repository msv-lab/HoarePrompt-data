#State of the program right berfore the function call: a, b, and c are integers such that 1 ≤ a, b, c ≤ 1500, representing the time intervals of the three garlands.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the greatest common divisor of the original values of `a` and `b`, `c` is an integer such that 1 ≤ `c` ≤ 1500.
    return a
    #The program returns the greatest common divisor 'a' of the original values of 'a' and 'b', where 'b' is 0.
#Overall this is what the function does:The function calculates and returns the greatest common divisor (GCD) of the two input integers `a` and `b` using the Euclidean algorithm. After executing, the function guarantees that `b` will be 0 and `a` will hold the GCD of the original values of `a` and `b`. The function does not use parameter `c`, which is mentioned in the annotations and is irrelevant to its operation. Since the inputs are constrained between 1 and 1500, it safely computes the GCD without any additional checks for validity or zero values for `a` or `b`.

