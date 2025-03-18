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
        
    #State: For each test case, `t` is updated based on the input values `a` and `b` such that it is the minimum number of 15-minute intervals required to satisfy the condition `t * 15 >= a + b * 4`. The value of `t` for each test case is printed. The initial value of `t` and the input values `a` and `b` for each test case are not retained after the loop completes.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `n` indicating the number of test cases, and for each test case, it reads two integers `a` and `b` from the input. The function calculates the minimum number of 15-minute intervals (`t`) required such that `t * 15 >= a + b * 4` and prints this value for each test case. The function does not return any value; it only prints the results. After processing all test cases, the initial values of `a`, `b`, and `t` for each test case are not retained.

