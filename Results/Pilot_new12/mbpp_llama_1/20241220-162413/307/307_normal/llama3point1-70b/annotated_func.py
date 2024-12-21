#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    idx = 1
    while True:
        triangular_num = idx * (idx + 1) // 2
        
        if len(str(triangular_num)) >= n:
            return idx
        
        idx += 1
        
    #State of the program after the loop has been executed: `idx` is the smallest value such that the string representation of `idx * (idx + 1) // 2` has a length greater than or equal to the original value of `n`, and the loop terminates with this `idx` value. The original value of `n` remains unchanged.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the smallest positive integer `idx` such that the string representation of the triangular number `idx * (idx + 1) // 2` has a length of at least `n`. The function does not modify the original value of `n` and will continue to increment `idx` until the length condition is met, at which point it will return the corresponding `idx` value. The return value is not limited to 1, 2, or 3, but rather any positive integer that satisfies the length condition for the given `n`. The function will always terminate with a return value, as the loop will continue indefinitely until the condition is met.

