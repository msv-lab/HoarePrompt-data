#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the function receives two integers x and y (0 ≤ x, y ≤ 99) representing the number of 1x1 and 2x2 application icons, respectively.
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
        
    #State: The function prints the minimum number of 2x2 slots needed for each test case, and the variable `t` is reset to the value of `b` at the start of each loop iteration, with `n` remaining unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y` representing the number of 1x1 and 2x2 application icons, respectively. It then calculates and prints the minimum number of 2x2 slots needed to accommodate all the icons for each test case.

