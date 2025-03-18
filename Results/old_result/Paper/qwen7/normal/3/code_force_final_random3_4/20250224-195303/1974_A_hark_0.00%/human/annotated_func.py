#State of the program right berfore the function call: a and b are non-negative integers representing the number of 1x1 and 2x2 icons, respectively.
def func_1(a, b):
    return a if a < b else b
    #The program returns the value of 'b' if 'a' is greater than or equal to 'b', otherwise it returns the value of 'a'
#Overall this is what the function does:The function accepts two non-negative integers `a` and `b`. It compares these values and returns `b` if `a` is greater than or equal to `b`, otherwise it returns `a`.

#State of the program right berfore the function call: x and y are non-negative integers representing the number of applications with 1 × 1 and 2 × 2 icons, respectively.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + bxsfory (where bxsfory1 = math.ceil(x / 15) + 1 and bxsfory = math.ceil(y / 2))
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is a non-negative integer greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is a non-negative integer greater than 0)
            else :
                print(0)
                #This is printed: 0
            #State: x and y are non-negative integers, where y is 0 and x is either greater than 0 or not greater than 0 (i.e., 0).
        #State: x and y are non-negative integers, where if x is 0, y is a non-negative integer greater than 0, and a is a list of integers. If x is not 0, then y is 0.
    #State: `x` and `y` are non-negative integers. If `x` is greater than 0 and less than or equal to `bxsfory * 15` and `y` is greater than 0, then `x` is adjusted according to specific rules (either set to twice the value of `x` or incremented by 5 based on the value of `x`). If `x` is 0, then `y` is a non-negative integer greater than 0. If `x` is not 0, then `y` is set to 0.
#Overall this is what the function does:The function processes the number of 1 × 1 and 2 × 2 application icons (represented by `x` and `y` respectively) and calculates the total number of rows needed to arrange these icons. It prints the result based on the given conditions. If both `x` and `y` are positive, it adjusts `x` according to specific rules and calculates the total rows. If only `y` is positive, it calculates the rows based on `y`. If only `x` is positive, it calculates the rows based on `x`. If neither `x` nor `y` is positive, it prints 0.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: Output State: `t` is an integer greater than 0.
    #
    #Explanation: The loop runs `t` times, where `t` is the input integer. Since the loop decreases the value of `t` by 1 with each iteration (implied by the problem's progression), after all iterations, `t` will be less than or equal to 0. However, since `t` starts as a positive integer between 1 and \(10^4\), and the loop continues as long as `t` is greater than 0, the final value of `t` after all iterations will still satisfy the condition of being an integer greater than 0.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t` (where 1 ≤ t ≤ 10^4). For each test case, it calls another function `func_2()`, which processes two integers `x` and `y` (where 0 ≤ x, y ≤ 99). After processing all test cases, the function ensures that the variable `t` is an integer greater than 0.

