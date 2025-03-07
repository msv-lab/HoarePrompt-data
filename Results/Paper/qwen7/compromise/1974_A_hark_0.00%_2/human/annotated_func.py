#State of the program right berfore the function call: a and b are non-negative integers representing the number of 1x1 and 2x2 icons, respectively.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller value between 'a' and 'b', where 'a' represents the number of 1x1 icons and 'b' represents the number of 2x2 icons.
#Overall this is what the function does:The function accepts two non-negative integer parameters, `a` and `b`, representing the number of 1x1 and 2x2 icons, respectively. It returns the smaller of the two values. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`.

#State of the program right berfore the function call: x and y are non-negative integers representing the number of 1 × 1 and 2 × 2 icons, respectively.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: integer (the ceiling of y divided by 2) + 0 or 1
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15)
            else :
                print(0)
                #This is printed: 0
            #State: x and y are non-negative integers. If x is greater than 0 and y is 0, then x remains greater than 0 and y remains 0. Otherwise, x and y retain their original values where either x is 0 or y is not 0.
        #State: x and y are non-negative integers. If x is 0 and y is a non-negative integer greater than 0, then x remains 0, y is set to a, and a is a list of integers. Otherwise, x and y retain their original values where either x is 0 or y is not 0.
    #State: x and y are non-negative integers. If both x and y are greater than 0, then `bxsfory` is equal to the ceiling of `y` divided by 2, `bxsfory1` is 1, `x` is updated to `x - bxsfory * 15 + y * 4`. If x is 0 and y is a non-negative integer greater than 0, then x remains 0, y is set to a, and a is a list of integers. Otherwise, x and y retain their original values where either x is 0 or y is not 0.
#Overall this is what the function does:The function processes two non-negative integers, `x` and `y`, representing the number of 1 × 1 and 2 × 2 icons, respectively. It calculates and prints the total number of icons based on specific conditions. If both `x` and `y` are greater than 0, it updates `x` and calculates the sum of the ceiling of `y` divided by 2 and 1. If only `y` is greater than 0, it calculates the ceiling of `y` divided by 2. If only `x` is greater than 0, it calculates the ceiling of `x` divided by 15. In all other cases, it prints 0.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, x and y are integers representing the number of applications with a 1 × 1 icon and the number of applications with a 2 × 2 icon, respectively.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: t test cases have been processed, but no specific output or state change within each test case is described.
#Overall this is what the function does:The function processes a specified number of test cases (determined by the input `t`). For each test case, it reads two integers `x` and `y`, representing the number of applications with 1 × 1 icons and 2 × 2 icons, respectively. After processing all test cases, it does not produce any output or return a value.

