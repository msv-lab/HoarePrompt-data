#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it receives two integers x and y (0 ≤ x, y ≤ 99) where x is the number of 1x1 application icons and y is the number of 2x2 application icons.
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
        
    #State: A series of printed values of `t` for each iteration of the loop, with `x` and `y` unchanged.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers representing the number of 1x1 and 2x2 application icons. For each test case, it calculates and prints the total number of icons required to meet or exceed the given number of 1x1 icons, considering the space occupied by 2x2 icons.

