#State of the program right berfore the function call: n and k are positive integers such that 1 <= n <= 10^9 and 0 <= k <= 8.**
def func():
    n, k = map(int, input().split())
    x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: After the loop executes, `n` is a positive integer such that `n` + 1 is not divisible by 10 to the power of `k`, `x` is adjusted accordingly, `n` is modified to satisfy `n % x != 0` condition
    print(n)
#Overall this is what the function does:The function `func` reads two positive integers `n` and `k` from input. It calculates the value of `x` as 10 to the power of `k`. Then, it increments `n` until `n` is divisible by `x`. Finally, it prints the updated value of `n`. The function does not explicitly return any value.

