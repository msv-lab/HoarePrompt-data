#State of the program right berfore the function call: n is a positive integer representing the number of digits in the triangular number.
def func_1(n):
    idx = 1
    while True:
        triangular_num = idx * (idx + 1) // 2
        
        if len(str(triangular_num)) >= n:
            return idx
        
        idx += 1
        
    #State of the program after the loop has been executed: `idx` is the smallest integer such that the triangular number `triangular_num` has at least `n` digits, `triangular_num` is equal to `idx * (idx + 1) // 2`, and `n` remains a positive integer representing the required number of digits.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the smallest integer `idx` such that the triangular number corresponding to `idx` has at least `n` digits. The function continues to compute triangular numbers until it finds one that meets this criterion. It does not handle cases where `n` is less than or equal to 0, which may lead to an infinite loop if such values are passed.

