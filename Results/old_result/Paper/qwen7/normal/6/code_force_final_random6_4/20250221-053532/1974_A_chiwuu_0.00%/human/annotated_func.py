#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
def func():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b * 2
        
        if t % 5 == 0:
            t = t // 5
        else:
            t = t // 5 + 1
        
        t1 = t * 15 - b * 4
        
        if t1 >= a:
            t = t
        else:
            t2 = a - t1
            if t2 % 15 == 0:
                t = t + t2 // 15
            else:
                t = t + t2 // 15 + 1
        
        print(t)
        
    #State: Output State: The final value of `t` after the loop executes all its iterations is determined by the cumulative effect of the operations performed within each iteration. Specifically, for each iteration, the value of `t` is updated based on the conditions provided. After all iterations, `t` will be the sum of the adjustments made during each iteration, starting from the initial value of `t` (which is `b * 2`), and modified by the logic inside the loop. Each iteration updates `t` based on the inputs `a` and `b` provided by the user, and the final value of `t` will reflect the total accumulated changes across all iterations.
    #
    #The exact final value of `t` cannot be precisely determined without knowing the specific values of `a` and `b` for each iteration, but it will be the result of repeatedly applying the logic described in the loop, starting from `t = b * 2` and adjusting `t` based on the conditions given.
#Overall this is what the function does:The function processes a series of test cases, where for each case, it reads two integers \(a\) and \(b\). It calculates an initial value for \(t\) as \(b \times 2\), then modifies \(t\) based on certain conditions involving \(a\) and \(b\). Specifically, it checks if \(t\) is divisible by 5; if not, it rounds up to the nearest multiple of 5. It then adjusts \(t\) further based on the difference between \(a\) and a calculated value \(t1\). If \(t1\) is less than \(a\), \(t\) is increased by the appropriate amount to make up for the shortfall, again rounding up to the nearest multiple of 15 if necessary. Finally, it prints the resulting value of \(t\) for each test case.

