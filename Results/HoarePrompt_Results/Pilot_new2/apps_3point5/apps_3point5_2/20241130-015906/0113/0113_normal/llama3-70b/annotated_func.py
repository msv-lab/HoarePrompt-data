#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n ≤ 10^9 and 0 ≤ k ≤ 8.**
def func():
    n, k = map(int, input().split())
    x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: Output State: n is a positive integer such that n % x = 0; k is an integer between 0 and 8; x is 10 raised to the power of k; n has been incremented by a multiple of x.
    print(n)
#Overall this is what the function does:The function `func` reads two positive integers `n` and `k` from input, where `n` ranges from 1 to 10^9 and `k` ranges from 0 to 8. It then calculates the smallest multiple of 10^k that is greater than or equal to `n` and prints this value.

