#State of the program right berfore the function call: a and b are values of any type that can be compared using the less than (<) operator.
def func_1(a, b):
    return a if a < b else b
    #The program returns `a` if `a` is less than `b`, otherwise it returns `b`.
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, which are values of any type that can be compared using the less than (<) operator. It returns the smaller of the two values. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x, y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + bxsfory (where bxsfory1 is 0 if x is less than or equal to 0, otherwise math.ceil(x / 15) + 1, and bxsfory is math.ceil(y / 2))
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is an integer between 1 and 99, and math.ceil(y / 2) is the smallest integer greater than or equal to y / 2)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is an integer between 1 and 99, and the result is an integer between 1 and 7)
            else :
                print(0)
                #This is printed: 0
            #State: *`x` and `y` are assigned the values of two input integers, each between 0 and 99 (inclusive), and at least one of `x` or `y` is 0 or less. Additionally, either `x` is not 0, or `y` is 0 or less. If `x` is greater than 0 and `y` is 0, then `y` remains 0. Otherwise, it is not the case that `x` is greater than 0 and `y` is 0, and the values of `x` and `y` remain unchanged.
        #State: *`x` and `y` are assigned the values of two input integers, each between 0 and 99 (inclusive), and at least one of `x` or `y` is 0 or less. If `x` is 0 and `y` is greater than 0, then `x` remains 0 and `y` remains greater than 0. Otherwise, either `x` is not 0, or `y` is 0 or less. If `x` is greater than 0 and `y` is 0, then `y` remains 0. In all other cases, the values of `x` and `y` remain unchanged.
    #State: *`x` and `y` are assigned the values of two input integers, each between 0 and 99 (inclusive). If both `x` and `y` are greater than 0, `x` is updated to `x - bxsfory * 15 + y * 4`, where `bxsfory` is the ceiling of `y / 2`, and `bxsfory1` is 0 if the new `x` is less than or equal to 0, otherwise `bxsfory1` is `math.ceil(x / 15) + 1`. If at least one of `x` or `y` is 0 or less, the values of `x` and `y` remain unchanged, except in the case where `x` is greater than 0 and `y` is 0, in which case `y` remains 0.
#Overall this is what the function does:The function `func_2` reads two non-negative integers `x` and `y` from the user input, each between 0 and 99 (inclusive). It then prints a value based on the following conditions:
- If both `x` and `y` are greater than 0, it calculates `bxsfory` as the ceiling of `y / 2`, updates `x` to `x - bxsfory * 15 + y * 4`, and calculates `bxsfory1` as 0 if the new `x` is less than or equal to 0, otherwise as `math.ceil(x / 15) + 1`. It then prints the sum of `bxsfory1` and `bxsfory`.
- If `x` is 0 and `y` is greater than 0, it prints the ceiling of `y / 2`.
- If `x` is greater than 0 and `y` is 0, it prints the ceiling of `x / 15`.
- If both `x` and `y` are 0 or if either `x` or `y` is less than or equal to 0, it prints 0.

#State of the program right berfore the function call: t is a non-negative integer such that 1 <= t <= 10^4.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `t` is a non-negative integer such that 1 <= t <= 10^4, `_` is `t-1`, and `func_2()` has been called `t` times.
#Overall this is what the function does:The function `func_3` reads an integer `t` from the user input, where `t` is a non-negative integer such that 1 <= t <= 10^4. It then calls the function `func_2` exactly `t` times. After the function concludes, `t` remains a non-negative integer within the specified range, and `func_2` has been executed `t` times. The function does not accept any parameters and does not return any value.

