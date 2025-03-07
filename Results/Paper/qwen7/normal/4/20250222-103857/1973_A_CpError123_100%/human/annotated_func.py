#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are non-negative integers such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
def func():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if (a + b + c) % 2 != 0:
            print(-1)
            continue
        
        x = (a + b + c) // 2
        
        y = a + b
        
        print(min(x, y))
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 500\) and `t` is now `0`, `a` is an integer from the input, `b` is an integer from the input, `c` is an integer from the input, the sum of `a`, `b`, and `c` is odd, `x` is equal to `(a + b + c) // 2`, `y` is equal to `a + b`.
    #
    #After all the iterations of the loop have finished, `t` will be decremented until it reaches `0`. Therefore, the final value of `t` will be `0`. The values of `a`, `b`, and `c` will be those provided by the last set of inputs processed within the loop, and the calculations for `x` and `y` will be based on these values.
#Overall this is what the function does:The function processes up to 500 test cases. For each test case, it reads three integers \(a\), \(b\), and \(c\). It checks if the sum of \(a\), \(b\), and \(c\) is even. If the sum is odd, it prints \(-1\) and moves to the next test case. Otherwise, it calculates \(x\) as half of the sum (integer division) and \(y\) as the sum of \(a\) and \(b\). Finally, it prints the minimum of \(x\) and \(y\). After processing all test cases, the function outputs nothing and ends.

