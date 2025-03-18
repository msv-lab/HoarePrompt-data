#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), and for each test case, n, a, and b are positive integers (1 ≤ n, a, b ≤ 10^9).
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
        
    #State: `t` is 0, `x` is the last list of integers read from the input, `n` is `x[0]`, `a` is `x[1]`, `b` is `x[2]`. If `a` ≥ `b`, `profit` is `n * a`. Otherwise, `profit` is `n * a + (b - a) * (k + 1) - k * (k + 1) / 2`, where `k` is `min(n - 1, b - a)`.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it takes three positive integers `n`, `a`, and `b`. It calculates a profit value based on these inputs. If `a` is greater than or equal to `b`, the profit is simply `n * a`. Otherwise, it calculates a more complex profit value involving the minimum of `n - 1` and `b - a`. The function prints the calculated profit for each test case. After processing all test cases, the function terminates with `t` set to 0.

