#State of the program right berfore the function call: The function should accept two parameters, x and y, where x and y are non-negative integers such that 0 <= x, y <= 99.
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
        
    #State: The loop will execute `n` times, and for each iteration, it will read two integers `a` and `b` from the input, perform the specified calculations, and print the final value of `t`. The values of `x` and `y` remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. Instead, it reads an integer `n` from the input, which specifies the number of iterations. For each iteration, it reads two integers `a` and `b` from the input, performs a series of calculations to determine a value `t`, and prints `t`. The values of `a` and `b` are processed independently in each iteration, and the function does not affect any external variables or parameters.

