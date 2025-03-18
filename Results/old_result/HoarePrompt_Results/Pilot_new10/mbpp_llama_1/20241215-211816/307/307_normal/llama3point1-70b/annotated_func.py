#State of the program right berfore the function call: n is a positive integer greater than or equal to 1.
def func_1(n):
    idx = 1
    while True:
        triangular_num = idx * (idx + 1) // 2
        
        if len(str(triangular_num)) >= n:
            return idx
        
        idx += 1
        
    #State of the program after the loop has been executed: The function returns the smallest `idx` such that the length of the string representation of the `idx`-th triangular number is greater than or equal to the original value of `n`. The value of `idx` is the same as the returned value. The original value of `n` remains unchanged.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the smallest index `idx` such that the string representation of the `idx`-th triangular number has a length of at least `n`. The function dynamically calculates this index without any predefined upper limit.

