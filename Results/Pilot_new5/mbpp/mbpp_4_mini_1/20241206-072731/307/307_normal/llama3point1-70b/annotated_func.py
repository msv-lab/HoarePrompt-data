#State of the program right berfore the function call: n is a positive integer representing the number of digits in the triangular number.
def func_1(n):
    idx = 1
    while True:
        triangular_num = idx * (idx + 1) // 2
        
        if len(str(triangular_num)) >= n:
            return idx
        
        idx += 1
        
    #State of the program after the loop has been executed: `idx` is the smallest integer such that the triangular number corresponding to `idx` has at least `n` digits, `triangular_num` is the value of the triangular number at that `idx`, and `n` remains a positive integer representing the number of digits in the triangular number.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the smallest integer `idx` such that the triangular number corresponding to `idx` has at least `n` digits. It does not handle the case where `n` is non-positive, which could lead to an infinite loop.

