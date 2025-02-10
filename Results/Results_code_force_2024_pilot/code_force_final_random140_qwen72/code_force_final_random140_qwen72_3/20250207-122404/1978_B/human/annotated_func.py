#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), and for each of the t test cases, n, a, and b are positive integers (1 ≤ n, a, b ≤ 10^9).
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
        
    #State: `t` is 0, and the loop has completed all its iterations. For each iteration, `x` was a list of integers read from the input, `n` was the first integer in the list `x`, `a` was the second integer in the list `x`, and `b` was the third integer in the list `x`. The `profit` was calculated based on the conditions provided in the loop: if `a` was greater than or equal to `b`, `profit` was `n * a`; otherwise, `profit` was updated to `n * a + (b - a) * (k + 1) - k * (k + 1) / 2`, where `k` was the minimum of `n - 1` and `b - a`. Each calculated `profit` was printed.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `a`, and `b`. It calculates a profit value based on these inputs: if `a` is greater than or equal to `b`, the profit is `n * a`; otherwise, the profit is adjusted using a formula that considers the difference between `a` and `b`. The calculated profit for each test case is printed. After processing all test cases, the function completes, and `t` is 0.

