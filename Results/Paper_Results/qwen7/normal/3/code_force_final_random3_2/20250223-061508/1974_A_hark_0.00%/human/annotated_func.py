#State of the program right berfore the function call: a and b are non-negative integers representing the number of 1x1 and 2x2 icons, respectively.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller value between 'a' and 'b', where 'a' represents the number of 1x1 icons and 'b' represents the number of 2x2 icons.
#Overall this is what the function does:The function accepts two non-negative integer parameters, `a` and `b`, representing the number of 1x1 and 2x2 icons, respectively. It returns the smaller of the two values. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`.

#State of the program right berfore the function call: x and y are non-negative integers representing the number of applications with 1x1 and 2x2 icon sizes, respectively.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: 2 + ceiling(y / 2)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is an integer greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15)
            else :
                print(0)
                #This is printed: 0
            #State: At least one of `x` or `y` is less than or equal to 0, and `x` is not equal to 0 or `y` is not greater than 0. If `x` is greater than 0 and `y` is 0, then `x` remains unchanged and `y` remains 0. Otherwise, `x` is not greater than 0 or `y` is equal to 0.
        #State: At least one of `x` or `y` is less than or equal to 0. If `x` is 0 and `y` is greater than 0, then `y` is unchanged and remains greater than 0. Otherwise, `x` is not greater than 0 or `y` is equal to 0.
    #State: `x` and `y` are integers. If both `x` and `y` are greater than 0, and `x` is greater than `bxsfory` * 15 + `y` * 4 where `bxsfory` is the ceiling value of `y` divided by 2, then `y` is set to twice its value. Otherwise, at least one of `x` or `y` is less than or equal to 0, and if `x` is 0 and `y` is greater than 0, `y` remains unchanged.
#Overall this is what the function does:The function reads two non-negative integers `x` and `y` from input, representing the number of applications with 1x1 and 2x2 icon sizes, respectively. It then calculates and prints the total number of applications based on specific conditions. If both `x` and `y` are greater than 0, it adjusts `x` based on `y` and calculates the total. If only `y` is greater than 0, it prints the ceiling value of `y` divided by 2. If only `x` is greater than 0, it prints the ceiling value of `x` divided by 15. If neither `x` nor `y` is greater than 0, it prints 0. The function does not return any value but prints the result directly.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, x and y are integers representing the number of applications with a 1 × 1 icon and the number of applications with a 2 × 2 icon, respectively.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: t must be greater than or equal to the total number of iterations the loop has executed.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y`, where `x` represents the number of applications with a 1 × 1 icon and `y` represents the number of applications with a 2 × 2 icon. The function processes this input data for each test case without returning any value.

