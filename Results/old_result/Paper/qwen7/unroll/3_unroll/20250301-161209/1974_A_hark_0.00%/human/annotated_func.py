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
        #This is printed: 1 + bxsfory
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is an input integer greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is a positive integer greater than 0)
            else :
                print(0)
                #This is printed: 0
            #State: `x` is an input integer, `y` is an input integer. If `x` is greater than 0 and `y` is 0, then `x` remains unchanged and `y` remains 0. Otherwise, either `x` is less than or equal to 0 or `y` is greater than 0, and both `x` and `y` remain their original values.
        #State: `x` and `y` are integers. If `x` is 0 and `y` is greater than 0, then `x` remains 0 and `y` remains greater than 0. Otherwise, `x` and `y` remain their original values.
    #State: Postcondition: `x` and `y` are integers. If `x` is greater than 0 and `y` is greater than 0, then `x` is adjusted to be an input integer greater than 0 minus `bxsfory` times 15 plus `y` times 4, where `bxsfory` is the ceiling value of `y` divided by 2, and `bxsfory1` is 1 if `x` is greater than 0, otherwise 0. If `x` is 0 and `y` is greater than 0, then `x` remains 0 and `y` remains greater than 0. Otherwise, `x` and `y` remain their original values.
#Overall this is what the function does:The function processes two non-negative integers \( x \) and \( y \), representing the number of 1 × 1 and 2 × 2 icons, respectively. It adjusts \( x \) based on the value of \( y \) and prints the sum of \( bxsfory \) and \( bxsfory1 \). If \( x \) is 0 and \( y \) is greater than 0, it prints \( bxsfory \). If \( x \) is greater than 0 and \( y \) is 0, it prints \( bxsfory1 \). In all other cases, it prints 0.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 10^4, and it remains assigned to its initial value after the loop has executed all the iterations. The variable `t` does not change within the loop, so its value stays the same.
#Overall this is what the function does:The function processes an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it calls another function `func_2()`. After processing all test cases, it outputs the initial value of `t`, which remains unchanged throughout the execution.

