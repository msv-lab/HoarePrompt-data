#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains two integers x and y (0 ≤ x, y ≤ 99) representing the number of 1x1 and 2x2 application icons, respectively.
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
        
    #State: The printed values of `t` for each of the `n` iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y` representing the number of 1x1 and 2x2 application icons, respectively. It calculates and prints the total number of 2x2 icons needed to accommodate both types of icons, ensuring that the total area covered by the icons is minimized.

