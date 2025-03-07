#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are non-negative integers such that 0 ≤ x, y ≤ 99.
def func():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b
        
        if t % 2 == 0:
            t = t // 2
        else:
            t = t // 2 + 1
        
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
        
    #State: Output State: After all iterations of the loop have finished, `t` will be the final value derived from the last iteration's calculations. The value of `t` will be based on the last input values of `a` and `b`, and will either be `b // 2` or `b // 2 + 1` depending on whether `b` was even or odd at the start. The exact value of `t` will also depend on the comparison between `t1` (calculated as `t * 15 - b * 4`) and `a`, and how many times the inner conditions were met during the iterations. If `t1 < a`, `t` will be incremented by the necessary amount to make `t1` at least equal to `a`, considering the division by 15 and potential remainder.
    #
    #In summary, `t` will reflect the cumulative effect of all iterations, with each step potentially adjusting `t` based on the current values of `a` and `b`, and the outcome of the comparisons within the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) and pairs of non-negative integers \( a \) and \( b \). For each test case, it calculates a final value for \( t \) based on the initial value of \( b \), which is adjusted if \( b \) is even or odd. It then compares this adjusted value with \( a \) and further modifies \( t \) if necessary to ensure \( t1 \geq a \), where \( t1 = t \times 15 - b \times 4 \). The function outputs the final value of \( t \) for each test case.

