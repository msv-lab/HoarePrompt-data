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
        
    #State: Output State: The value of `t` will be 0, as the loop runs from `range(t)`, and after all iterations, `t` will reach 0 since each iteration decreases `t` by 1. For each remaining value of `t`, the same process of taking three integers `a`, `b`, and `c` as input, checking if their sum is even, and then calculating `x` as `(a + b + c) // 2` and `y` as `a + b` will occur. If the sum is odd, `-1` will be printed and the loop will continue with the next value of `t`. After all iterations, if there are no more values of `t`, the loop ends, and `t` is set to 0. Variables `a`, `b`, `c`, `x`, and `y` will retain their last computed values based on the last set of inputs provided before `t` became 0.
    #
    #In simpler terms, after all iterations, `t` will be 0, and the final values of `a`, `b`, `c`, `x`, and `y` will be those from the last set of inputs processed before `t` reached 0.
#Overall this is what the function does:The function reads multiple test cases where each test case consists of three integers \(a\), \(b\), and \(c\). It checks if the sum of these integers is even. If the sum is even, it calculates two values: \(x\) as half of the sum and \(y\) as the sum of \(a\) and \(b\). It then prints the minimum of \(x\) and \(y\). If the sum is odd, it prints \(-1\). After processing all test cases, the function sets the counter \(t\) to 0. The final output consists of the results for each valid test case.

