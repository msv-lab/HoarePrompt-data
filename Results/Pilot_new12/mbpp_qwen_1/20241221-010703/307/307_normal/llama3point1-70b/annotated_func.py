#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    idx = 1
    while True:
        triangular_num = idx * (idx + 1) // 2
        
        if len(str(triangular_num)) >= n:
            return idx
        
        idx += 1
        
    #State of the program after the loop has been executed: `n` is a positive integer, `idx` is the smallest integer such that the length of the string representation of the triangular number corresponding to `idx` is at least `n`, and `triangular_num` is the triangular number corresponding to `idx`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and returns the smallest integer `idx` such that the length of the string representation of the `idx`-th triangular number is at least `n`. The function iterates starting from `idx = 1` and increments `idx` until the condition `len(str(triangular_num)) >= n` is met, where `triangular_num` is calculated as `idx * (idx + 1) // 2`. If `n` is 1, the function returns `idx` as 1 because the first triangular number (1) has a string length of 1. For larger values of `n`, the function continues incrementing `idx` until the condition is satisfied, returning the resulting `idx`.

