#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    while t:
        x = list(map(int, input().split(' ')))
        
        n = x[0]
        
        a = x[1]
        
        b = x[2]
        
        profit = n * a
        
        if a >= b:
            print(profit)
        else:
            k = b - a
            k = min(n - 1, k)
            profit = profit + (b - a) * (k + 1) - k * (k + 1) / 2
            print(int(profit))
        
        t -= 1
        
    #State: Output State: `t` is 0, and the remaining variables (`x`, `n`, `a`, `b`, `profit`, and `k`) are undefined because the loop has finished executing, and `t` is no longer greater than 0.
    #
    #This means that after all iterations of the loop have finished, `t` will be 0 since it is decremented by 1 in each iteration until it reaches 0. At this point, no further inputs are processed, and the values of `x`, `n`, `a`, `b`, `profit`, and `k` are undefined as they were last updated within the loop body and are no longer relevant once the loop terminates.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \( n \), \( a \), and \( b \). For each test case, it calculates a profit based on the values of \( n \) and \( a \). If \( a \geq b \), it prints the initial profit \( n \times a \). Otherwise, it calculates a modified profit considering the difference \( b - a \) and prints the result. After processing all test cases, the function outputs nothing and leaves all local variables undefined.

