#State of the program right berfore the function call: n is a non-negative integer (0 ≤ n ≤ 2,000,000,000) and k is a positive integer (1 ≤ k ≤ 9).
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is a multiple of 10 raised to the power of `k`, `w` is the count of how many times `n` was not divisible by 10 raised to the power of `k` before the loop finished, and `k` remains the input positive integer (1 ≤ k ≤ 9)
    print(w)
#Overall this is what the function does:The function accepts a non-negative integer `n` (0 ≤ n ≤ 2,000,000,000) and a positive integer `k` (1 ≤ k ≤ 9), counts how many times `n` is not divisible by 10 raised to the power of `k` by repeatedly dividing `n` by 10 until it becomes divisible, and prints the count `w`.

