#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9, and k is a non-negative integer such that 0 ≤ k ≤ 8.
def func():
    n, k = map(int, input().split())
    x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: `n` is a positive integer such that `n` is now a multiple of `10`, `n` must have been incremented until it became a multiple of `10`, and the original value of `n` was not a multiple of `10`.
    print(n)
#Overall this is what the function does:The function accepts two integers, `n` (a positive integer between 1 and 10^9) and `k` (a non-negative integer between 0 and 8), provided via standard input. It increments `n` until it becomes a multiple of `10` raised to the power of `k`. Finally, it prints the modified value of `n`. The function does not handle cases where the original `n` is already a multiple of `10^k`, as it will still enter the loop and increment, which can lead to unexpected results if `k` is greater than 0.

