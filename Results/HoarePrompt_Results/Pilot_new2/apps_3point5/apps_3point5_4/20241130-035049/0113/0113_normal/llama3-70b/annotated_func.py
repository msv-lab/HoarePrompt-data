#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer.**
def func():
    n, k = map(int, input().split())
    x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: 'n' is such that 'n % x' is equal to 0
    print(n)
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from input, calculates `x` as 10 raised to the power of `k`, then increments `n` until it is divisible by `x`. After that, it prints out the final value of `n`. The function does not accept any parameters and has no return value.

