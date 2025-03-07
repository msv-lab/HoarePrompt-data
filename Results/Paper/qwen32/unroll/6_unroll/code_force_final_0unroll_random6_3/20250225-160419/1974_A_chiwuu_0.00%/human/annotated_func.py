#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, x and y are integers such that 0 <= x, y <= 99.
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
        
    #State: the series of printed values of `t` for each of the `n` test cases.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then calculates and prints a value `t` for each test case based on the given logic, which involves operations including multiplication, division, and conditional checks. The final state of the program is a series of printed values of `t` corresponding to each test case.

