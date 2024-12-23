#State of the program right berfore the function call: n is a positive integer representing the number of digits in the triangular number.
def func_1(n):
    k = 1
    while True:
        triangular_number = k * (k + 1) // 2
        
        if len(str(triangular_number)) == n:
            return k
        
        k += 1
        
    #State of the program after the loop has been executed: `n` is a positive integer representing the number of digits in the triangular number, `k` is the smallest integer such that the triangular number `triangular_number` (calculated as `k * (k + 1) // 2`) has exactly `n` digits. If the loop executed `m` times, `k` would be `m + 1`, where `triangular_number` would be the first triangular number with `n` digits.
#Overall this is what the function does:The function `func_1` accepts a single parameter `n`, which is a positive integer representing the number of digits in a triangular number. The function returns the smallest positive integer `k` such that the `k`-th triangular number, calculated as `k * (k + 1) // 2`, has exactly `n` digits. The function continuously computes triangular numbers starting from `k = 1` and checks their digit count until it finds one that has exactly `n` digits. There are no specific returns for cases where no triangular number exists with `n` digits—if `n` is too large, the function may run indefinitely.

