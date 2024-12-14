#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    k = 1
    while True:
        triangular_number = k * (k + 1) // 2
        
        if len(str(triangular_number)) == n:
            return k
        
        k += 1
        
    #State of the program after the loop has been executed: `k` is the smallest integer such that the length of the string representation of the triangular number `k * (k + 1) // 2` is equal to `n`, and `triangular_number` is `k * (k + 1) // 2`.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the smallest integer `k` such that the length of the string representation of the triangular number `k * (k + 1) // 2` is equal to `n`.

