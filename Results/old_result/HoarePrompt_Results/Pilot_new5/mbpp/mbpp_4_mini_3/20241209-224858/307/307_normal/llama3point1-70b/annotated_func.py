#State of the program right berfore the function call: n is a positive integer representing the number of digits in the triangular number.
def func_1(n):
    idx = 1
    while True:
        triangular_num = idx * (idx + 1) // 2
        
        if len(str(triangular_num)) >= n:
            return idx
        
        idx += 1
        
    #State of the program after the loop has been executed: `idx` is the first integer such that the triangular number corresponding to `idx` has at least `n` digits, `triangular_num` is the triangular number of the final `idx`, and the initial value of `n` is a positive integer.
#Overall this is what the function does:The function accepts a positive integer `n` and calculates the index `idx` of the first triangular number that has at least `n` digits. It continues to calculate triangular numbers until one is found that meets the digit requirement, returning that index. The function does not have a cap on `n`, so it could potentially run indefinitely if `n` is excessively large and no corresponding triangular number exists within a reasonable range.

