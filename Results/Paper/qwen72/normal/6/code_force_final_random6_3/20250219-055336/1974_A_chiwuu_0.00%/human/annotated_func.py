#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, x and y are integers such that 0 <= x, y <= 99.
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
        
    #State: After the loop executes all `n` iterations, `i` is `n-1`, and `t` is updated based on the final values of `a` and `b` from the last iteration. If `t % 5 == 0`, `t` is updated to `b * 2 // 5`. Otherwise, `t` is updated to `b * 2 // 5 + 1`. `t1` is calculated as `t * 15 - b * 4`. If `t1 >= a`, `t` remains unchanged. Otherwise, `t2` is set to `a - t1`, and if `t2 % 15 == 0`, `t` is updated to `t + t2 // 15`. If `t2 % 15 != 0`, `t` is updated to `t + t2 // 15 + 1`. The values of `x` and `y` remain unchanged as they are not affected by the loop.
#Overall this is what the function does:The function `func` processes `n` test cases, where `n` is an integer provided by the user. For each test case, it reads two integers `a` and `b` from the user input. It calculates a value `t` based on `b` and updates `t` to ensure that `t * 15 - b * 4` is at least `a`. The final value of `t` for each test case is printed. The function does not return any value. After processing all test cases, the variables `a`, `b`, and `t` are no longer relevant, and the function concludes.

