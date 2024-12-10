#State of the program right berfore the function call: n is a positive integer representing the number of digits.
def func_1(n):
    k = 1
    while True:
        triangular_number = k * (k + 1) // 2
        
        if len(str(triangular_number)) == n:
            return k
        
        k += 1
        
    #State of the program after the loop has been executed: `n` is the original positive integer representing the number of digits, `k` is the smallest integer such that the triangular number corresponding to `k` has exactly `n` digits, `triangular_number` is the triangular number for that `k`.
#Overall this is what the function does:The function accepts a positive integer `n` and finds the smallest integer `k` such that the k-th triangular number (calculated as `k * (k + 1) // 2`) has exactly `n` digits. It returns the value of `k`, which can be any positive integer starting from 1, and continues until the condition is met.

