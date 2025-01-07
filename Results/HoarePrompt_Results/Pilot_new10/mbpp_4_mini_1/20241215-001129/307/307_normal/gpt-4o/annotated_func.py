#State of the program right berfore the function call: n is a positive integer representing the number of digits in the triangular number.
def func_1(n):
    k = 1
    while True:
        triangular_number = k * (k + 1) // 2
        
        if len(str(triangular_number)) == n:
            return k
        
        k += 1
        
    #State of the program after the loop has been executed: `k` is the first integer after all iterations where the triangular number has `n` digits, `n` stays as the original positive integer for number of digits; the triangular number is equal to the sum of numbers from 1 to `k`, leading to a triangular number with exactly `n` digits.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the smallest integer `k` such that the k-th triangular number has exactly `n` digits.

