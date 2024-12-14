#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    idx = 1
    while True:
        triangular_num = idx * (idx + 1) // 2
        
        if len(str(triangular_num)) >= n:
            return idx
        
        idx += 1
        
    #State of the program after the loop has been executed: `n` is a positive integer, `idx` is the smallest integer such that the length of the string representation of the triangular number with index `idx` is at least `n`, and `triangular_num` is the triangular number corresponding to this `idx`.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the smallest integer `idx` such that the length of the string representation of the triangular number with index `idx` is at least `n`.

