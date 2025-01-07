#State of the program right berfore the function call: n is a positive integer representing the number of digits in the triangular number.
def func_1(n):
    k = 1
    while True:
        triangular_number = k * (k + 1) // 2
        
        if len(str(triangular_number)) == n:
            return k
        
        k += 1
        
    #State of the program after the loop has been executed: `k` is the smallest integer such that the triangular number corresponding to `k` has `n` digits, `triangular_number` is the triangular number of `k`, and `n` is a positive integer representing the number of digits in the triangular number.
#Overall this is what the function does:The function accepts a positive integer `n`, which represents the number of digits in a triangular number. It returns the smallest integer `k` such that the triangular number corresponding to `k` has exactly `n` digits. The function continues to calculate triangular numbers until it finds one that meets this condition. There are no checks for invalid input, so if `n` is less than 1 or not an integer, the behavior is undefined.

