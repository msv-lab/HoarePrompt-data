#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains two integers x and y (0 ≤ x, y ≤ 99), where x is the number of applications with a 1 × 1 icon and y is the number of applications with a 2 × 2 icon.
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
        
    #State: 
#Overall this is what the function does:The function processes a series of test cases, each defined by the number of 1x1 and 2x2 application icons. For each test case, it calculates and outputs the total number of icons required, ensuring that the number of 1x1 icons is accommodated after placing the 2x2 icons.

