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
        
    #State: Output State: The final value of `t` after the loop has executed all its iterations will depend on the values of `n`, `a`, and `b` for each iteration. After the loop completes, `t` will be updated based on the conditions provided within the loop body. Specifically, `t` is initially set to `b * 2`, then adjusted according to the following rules:
    #
    #1. If `t % 5 == 0`, `t` is set to `t // 5`.
    #2. Otherwise, `t` is set to `t // 5 + 1`.
    #3. Then, `t1` is calculated as `t * 15 - b * 4`.
    #4. If `t1 >= a`, `t` remains unchanged.
    #5. Otherwise, `t2` is calculated as `a - t1`.
    #6. If `t2 % 15 == 0`, `t` is increased by `t2 // 15`.
    #7. Otherwise, `t` is increased by `t2 // 15 + 1`.
    #
    #After all iterations, `t` will reflect the cumulative effect of these updates based on the inputs provided for each iteration of the loop. The exact value of `t` cannot be determined without knowing the specific values of `n`, `a`, and `b` for each iteration, but it will be the result of applying the above logic iteratively for `n` times.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \(a\) and \(b\). For each test case, it calculates and updates the value of \(t\) based on specific conditions. Initially, \(t\) is set to \(2 \times b\), then it is adjusted based on whether \(t\) is divisible by 5, and further modified based on the comparison between \(t1 = t \times 15 - b \times 4\) and \(a\). Finally, the function prints the updated value of \(t\) for each test case.

