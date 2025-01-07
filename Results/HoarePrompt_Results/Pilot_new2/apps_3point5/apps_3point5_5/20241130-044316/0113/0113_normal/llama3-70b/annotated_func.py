#State of the program right berfore the function call: n and k are positive integers such that 1 <= n <= 10^9 and 0 <= k <= 8.**
def func():
    n, k = map(int, input().split())
    x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: `n` is divisible by 10 to the power of `k`, where `k` is the original value of `k` and `n` is the final adjusted value after the loop execution.
    print(n)
#Overall this is what the function does:The function `func` accepts two positive integers `n` and `k`, where 1 <= n <= 10^9 and 0 <= k <= 8. It reads input values for `n` and `k`, calculates the value of x as 10 to the power of k, then increments `n` until it is divisible by x. Finally, it prints the adjusted value of `n`. The function lacks a return statement, so it does not explicitly return any value.

