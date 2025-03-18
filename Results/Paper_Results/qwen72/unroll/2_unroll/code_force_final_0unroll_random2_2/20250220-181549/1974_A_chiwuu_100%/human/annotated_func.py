#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, x and y are integers such that 0 <= x, y <= 99.
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
        
    #State: For each test case, the value of t is adjusted based on the conditions inside the loop, but the values of n, x, and y remain unchanged. After all iterations of the loop, t will be the final computed value for each test case, and the loop will have printed this value n times.
#Overall this is what the function does:The function `func` reads an integer `n` indicating the number of test cases. For each test case, it reads two integers `x` and `y` (0 <= x, y <= 99). It then computes a value `t` based on the conditions inside the loop and prints this value for each test case. The function does not return any value, but it prints the computed `t` for each of the `n` test cases. After the function concludes, the values of `n`, `x`, and `y` remain unchanged, and the program state includes the printed values of `t` for each test case.

