#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9, and k is a non-negative integer such that 0 ≤ k ≤ 8.
def func():
    n, k = map(int, input().split())
    x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: `n` is the smallest multiple of 10 greater than or equal to the original value of `n`, `k` remains unchanged, `x` is 10.
    print(n)
#Overall this is what the function does:The function accepts two integers `n` (a positive integer within the range 1 to 10^9) and `k` (a non-negative integer within the range 0 to 8). It finds the smallest integer greater than or equal to `n` that is a multiple of 10 raised to the power of `k`. The function prints this resulting integer.

