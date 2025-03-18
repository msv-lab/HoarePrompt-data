#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, x and y are integers such that 0 <= x, y <= 99.
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
        
    #State: After the loop executes all iterations, `t` is an integer that has been updated based on the logic within the loop for each of the `n` iterations. The values of `x` and `y` remain integers such that 0 <= `x`, `y` <= 99, and `n` is the input integer that determines the number of iterations. The loop variable `i` will be `n - 1` after the last iteration. For each iteration, `a` and `b` are read from input, and `t` is updated as follows:
#Overall this is what the function does:The function `func` reads an integer `n` from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the input. It then calculates and prints an integer `t` for each test case, where `t` is determined based on the values of `a` and `b` through a series of arithmetic operations and conditions. The final value of `t` is such that it satisfies the conditions within the function, and it is printed for each test case. The function does not return any value.

