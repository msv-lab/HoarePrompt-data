#State of the program right berfore the function call: a and b are integers.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller of the two integers a or b.
#Overall this is what the function does:The function accepts two integer parameters and returns the smaller of the two.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x <= 99 and 0 <= y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + bxsfory (where bxsfory1 is 0 if x <= 0 else math.ceil(x / 15) + 1, and bxsfory is math.ceil(y / 2))
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is a non-negative integer greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is a non-negative integer greater than 0 and less than or equal to 99)
            else :
                print(0)
                #This is printed: 0
            #State: `x` and `y` are non-negative integers such that 0 <= x <= 99 and 0 <= y <= 99. At least one of `x` or `y` is 0. If `x` is greater than 0 and `y` is 0, the conditions remain the same. Otherwise, it is not the case that `x` is greater than 0 and `y` is equal to 0.
        #State: `x` and `y` are non-negative integers such that 0 <= x <= 99 and 0 <= y <= 99. At least one of `x` or `y` is 0. If `x` is 0 and `y` is greater than 0, the conditions remain the same. Otherwise, it is not the case that `x` is greater than 0 and `y` is equal to 0.
    #State: `x` and `y` are non-negative integers such that 0 <= x <= 99 and 0 <= y <= 99. If both `x` and `y` are greater than 0, then `x` is updated to `x - bxsfory * 15 + y * 4` and `y` remains the same, where `bxsfory` is the ceiling of `y / 2`, and `bxsfory1` is `0` if `x` <= 0 else `math.ceil(x / 15) + 1`. Otherwise, at least one of `x` or `y` is 0, and the values of `x` and `y` remain unchanged.
#Overall this is what the function does:The function `func_2` reads two non-negative integers `x` and `y` from the input, where `0 <= x <= 99` and `0 <= y <= 99`. It then calculates and prints a value based on the conditions of `x` and `y`. If both `x` and `y` are greater than 0, it computes a specific formula involving `x` and `y` and prints the result. If either `x` or `y` is 0, it prints a simpler value derived from the non-zero variable or 0 if both are 0.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of two integers x and y such that 0 <= x, y <= 99.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `t` is 0, `x` and `y` are integers such that 0 <= `x`, `y` <= 99
#Overall this is what the function does:The function `func_3` reads an integer `t` representing the number of test cases. For each of the `t` test cases, it processes two integers `x` and `y` (where 0 <= x, y <= 99) by calling `func_2`. The overall effect is that for each test case, some action is performed (as defined in `func_2`), although the specific action is not detailed in the provided code.

