#State of the program right berfore the function call: n is a positive integer representing the number of digits.
def func_1(n):
    idx = 1
    while True:
        triangular_num = idx * (idx + 1) // 2
        
        if len(str(triangular_num)) >= n:
            return idx
        
        idx += 1
        
    #State of the program after the loop has been executed: `idx` is the minimum integer for which the triangular number is at least n digits, `triangular_num` is k * (k + 1) // 2, n is a positive integer representing the number of digits.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the smallest integer `idx` such that the triangular number corresponding to `idx` has at least `n` digits. The function continues to increment `idx` until it finds a triangular number whose string representation has a length greater than or equal to `n`. There are no cases where it returns 1 or 2; it only returns the value of `idx` once the condition is met.

