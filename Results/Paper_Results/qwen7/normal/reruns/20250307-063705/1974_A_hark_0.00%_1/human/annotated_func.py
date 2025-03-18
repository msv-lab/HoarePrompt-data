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
        #This is printed: 1 + (y // 2)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where math.ceil() rounds up y / 2 to the nearest integer)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: 1
            else :
                print(0)
                #This is printed: 0
            #State: Postcondition: `x` is an input integer, `y` is an input integer. If `x` is greater than 0 and `y` is 0, then `y` remains 0. Otherwise, `x` is less than or equal to 0 or `y` is greater than 0.
        #State: Postcondition: `x` is an input integer, `y` is an input integer. If `x` is 0 and `y` is greater than 0, then `y` remains greater than 0. Otherwise, `x` is less than or equal to 0 or `y` is greater than 0.
    #State: Postcondition: `x` is an input integer and `y` is an input integer. If `x` is greater than 0 and `y` is greater than 0, and additionally `x` is greater than `bxsfory` * 15 + `y` * 4 where `bxsfory` is the ceiling value of `y` divided by 2, then specific conditions related to `x` and `y` are met as per the if part. Otherwise, either `x` is less than or equal to 0 or `y` is greater than 0.
#Overall this is what the function does:The function processes two non-negative integers, `x` and `y`, representing the number of 1 × 1 and 2 × 2 icons, respectively. It calculates and prints the total number of 1 × 1 icons required based on the given conditions. Specifically:
- If both `x` and `y` are greater than 0, it calculates the number of 1 × 1 icons needed to match the value of `y` and adjusts `x` accordingly.
- If only `y` is greater than 0, it calculates the number of 1 × 1 icons needed to match `y`.
- If only `x` is greater than 0, it calculates the number of 1 × 1 icons needed to match `x`.
- If neither `x` nor `y` is greater than 0, it prints 0.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, x and y are integers representing the number of applications with a 1 × 1 icon and the number of applications with a 2 × 2 icon, respectively.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: Output State: `t` must be greater than 0.
    #
    #Natural Language Explanation: The loop continues to execute as long as `t` is greater than 0. Since the loop runs for all iterations as long as this condition holds true, the final output state after all iterations will still require that `t` must be greater than 0. There are no changes made inside the loop that would affect the value of `t`, so its initial condition remains the same.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it calls another function `func_2()` without any explicit return value. After processing all test cases, the function ensures that the variable `t` remains greater than 0.

