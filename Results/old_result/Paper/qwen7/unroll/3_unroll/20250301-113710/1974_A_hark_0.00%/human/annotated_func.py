#State of the program right berfore the function call: a and b are non-negative integers representing the number of 1x1 and 2x2 icons, respectively.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller value between 'a' and 'b', where 'a' represents the number of 1x1 icons and 'b' represents the number of 2x2 icons.
#Overall this is what the function does:The function accepts two non-negative integer parameters, `a` and `b`, representing the number of 1x1 and 2x2 icons, respectively. It returns the smaller of the two values. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`.

#State of the program right berfore the function call: x and y are non-negative integers representing the number of applications with 1 × 1 and 2 × 2 icons, respectively.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + math.ceil(y / 2)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is a non-negative integer greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15)
            else :
                print(0)
                #This is printed: 0
            #State: x and y are non-negative integers representing the number of applications with 1 × 1 and 2 × 2 icons, respectively. If x is greater than 0 and y is 0, x represents the number of 1 × 1 icons and y remains 0. Otherwise, x and y represent the number of applications with 1 × 1 and 2 × 2 icons, respectively, and either x is 0 or y is not 0.
        #State: x and y are non-negative integers representing the number of applications with 1 × 1 and 2 × 2 icons, respectively. If x is 0, then y represents the number of 2 × 2 icons (and y > 0). Otherwise, x and y represent the number of 1 × 1 and 2 × 2 icons, respectively, with at least one of them being non-zero.
    #State: `bxsfory1` and `bxsfory` are calculated based on the values of `x` and `y`. If `x > 0` and `y > 0`, then `bxsfory1` is `math.ceil(x / 15) + 1` if `x > 0` else 0, `bxsfory` is `math.ceil(y / 2)`, and `x` is updated to `x - bxsfory * 15 + y * 4`. If `x` is 0, then `y` represents the number of 2 × 2 icons (and `y > 0`). Otherwise, `x` and `y` represent the number of 1 × 1 and 2 × 2 icons, respectively, with at least one of them being non-zero.
#Overall this is what the function does:The function calculates and returns the total number of applications arranged in a grid using 1 × 1 and 2 × 2 icons. It takes the number of 1 × 1 icons (`x`) and the number of 2 × 2 icons (`y`) as input, where both are non-negative integers. Depending on the values of `x` and `y`, it computes the number of rows needed to arrange these icons in a grid and returns this total number of rows. If `x` is greater than 0 and `y` is greater than 0, it adjusts `x` based on the number of 2 × 2 icons and calculates the total rows accordingly. If `x` is 0, it only considers the 2 × 2 icons, and if `y` is 0, it only considers the 1 × 1 icons. In all cases, it ensures that the arrangement fits the given number of icons.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: Output State: `t` is an integer between 1 and 10^4 inclusive, and it has been used to control the number of iterations in the loop. After the loop executes all the iterations, no other variables are affected by the loop, so their states remain unchanged. The loop itself does not change any variable's value; it only calls `func_2()` for `t` times.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t` (where 1 ≤ t ≤ 10^4). For each test case, it calls another function `func_2()`. After processing all test cases, the function does not return any specific value and leaves the original variables (x and y) unchanged.

