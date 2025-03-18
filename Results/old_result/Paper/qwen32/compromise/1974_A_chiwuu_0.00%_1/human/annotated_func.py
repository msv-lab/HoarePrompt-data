#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains two integers x and y (0 ≤ x, y ≤ 99) where x is the number of 1x1 application icons and y is the number of 2x2 application icons.
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
        
    #State: the final values of `t` for each of the `t` test cases, each on a new line.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it receives two integers `x` and `y`, where `x` is the number of 1x1 application icons and `y` is the number of 2x2 application icons. It calculates and prints the minimum number of 5x5 grids required to cover all the icons for each test case.

