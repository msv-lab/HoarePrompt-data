#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, x and y are integers such that 0 <= x, y <= 99.
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
        
    #State: After all iterations of the loop, `i` is equal to `n - 1`, and the loop has processed `n` pairs of inputs (`a`, `b`). For each iteration, the variable `t` is updated based on the conditions within the loop. Specifically, for each pair of inputs (`a`, `b`), `t` is initially set to `b // 2` if `b` is even, or `(b // 2) + 1` if `b` is odd. Then, `t1` is calculated as `t * 15 - b * 4`. If `t1` is greater than or equal to `a`, `t` remains unchanged. If `t1` is less than `a`, `t` is updated to `t + t2 // 15` if `t2 % 15 == 0`, or `t + t2 // 15 + 1` if `t2 % 15 != 0`, where `t2` is `a - t1`. The final value of `t` for each iteration is printed. The variables `x` and `y` remain unchanged, and `n` is the total number of iterations performed.
#Overall this is what the function does:The function `func` reads an integer `n` indicating the number of test cases, and for each test case, it reads two integers `a` and `b`. It then calculates and prints a value `t` for each test case. The value of `t` is determined based on the following logic: `t` is initially set to `b // 2` if `b` is even, or `(b // 2) + 1` if `b` is odd. Then, a value `t1` is computed as `t * 15 - b * 4`. If `t1` is greater than or equal to `a`, `t` remains unchanged. Otherwise, `t` is incremented by the ceiling of `(a - t1) / 15`. The function does not return any value; it only prints the calculated `t` for each test case. After processing all `n` test cases, the function completes its execution.

