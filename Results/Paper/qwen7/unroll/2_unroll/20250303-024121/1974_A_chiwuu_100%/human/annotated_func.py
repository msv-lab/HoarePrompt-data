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
        
    #State: Output State: The value of `t` after all iterations of the loop have completed, which depends on the values of `a` and `b` for each iteration. Specifically, `t` is updated based on the conditions provided in the loop body. If `t1` (calculated as `t * 15 - b * 4`) is greater than or equal to `a`, then `t` remains unchanged. Otherwise, `t` is increased by the result of the calculation involving `a - t1`. The final value of `t` will be the sum of its original value and any increments calculated during the loop iterations.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers \(a\) and \(b\). For each test case, it calculates a value \(t\) based on certain conditions and prints the final value of \(t\). Initially, \(t\) is set to \(b\), and it is adjusted based on whether \(t \times 15 - b \times 4\) is greater than or equal to \(a\). If not, \(t\) is incremented further depending on the remainder when \(a - t \times 15 + b \times 4\) is divided by 15. The function ultimately outputs the final value of \(t\) for each test case.

