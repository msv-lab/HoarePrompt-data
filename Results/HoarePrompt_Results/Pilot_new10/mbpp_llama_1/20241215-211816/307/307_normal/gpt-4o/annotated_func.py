#State of the program right berfore the function call: n is a positive integer greater than 0.
def func_1(n):
    k = 1
    while True:
        triangular_number = k * (k + 1) // 2
        
        if len(str(triangular_number)) == n:
            return k
        
        k += 1
        
    #State of the program after the loop has been executed: `n` is the original target length, `k` is the value for which the string representation of `k * (k + 1) // 2` has a length of `n`, and the loop has ended with `k` being returned.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the smallest integer `k` for which the string representation of the `k`-th triangular number has a length of `n`. It does not handle non-positive integers or non-integers explicitly and may enter an infinite loop or produce incorrect results for these inputs.

