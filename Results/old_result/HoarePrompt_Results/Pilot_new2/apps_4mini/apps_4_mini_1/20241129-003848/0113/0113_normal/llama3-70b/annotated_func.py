#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9, and k is a non-negative integer such that 0 ≤ k ≤ 8.
def func():
    n, k = map(int, input().split())
    x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: `n` is a multiple of 10, if the original value of `n` was not a multiple of 10, then `n` has been incremented to the next highest multiple of 10.
    print(n)
#Overall this is what the function does:The function accepts two parameters, `n` (a positive integer between 1 and 10^9) and `k` (a non-negative integer between 0 and 8), and increments `n` until it becomes a multiple of `10^k`. It then prints the resulting value of `n`. If `n` is already a multiple of `10^k`, it will remain unchanged.

