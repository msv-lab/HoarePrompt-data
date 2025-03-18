#State of the program right berfore the function call: a and b are values of any type that can be compared using the < operator.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller value between `a` and `b` if `a` is less than `b`, otherwise it returns `b`.
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, which are values of any type that can be compared using the `<` operator. It returns the smaller value between `a` and `b`. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x, y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: an integer between 1 and 83 (where `bxsfory1` is 0 if the updated `x` is less than or equal to 0, otherwise `math.ceil(x / 15) + 1`, and `bxsfory` is `math.ceil(y / 2)`)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is a non-negative integer greater than 0 and less than or equal to 99)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is a non-negative integer greater than 0 and less than or equal to 99, and the output will be one of the integers 1, 2, 3, 4, 5, 6, or 7)
            else :
                print(0)
                #This is printed: 0
            #State: *`x` and `y` are non-negative integers such that 0 <= x, y <= 99, and `x` and `y` are now assigned the values provided by the user input. If `x` > 0 and `y` == 0, no changes are made to `x` and `y`. Otherwise, either `x` is 0, or `y` is not 0, and no changes are made to `x` and `y`.
        #State: *`x` and `y` are non-negative integers such that 0 <= x, y <= 99, and `x` and `y` are now assigned the values provided by the user input. If `x` is 0 and `y` is greater than 0, no changes are made to `x` and `y`. If `x` is greater than 0 and `y` is 0, no changes are made to `x` and `y`. Otherwise, either `x` is 0, or `y` is not 0, and no changes are made to `x` and `y`.
    #State: *`x` and `y` are non-negative integers such that 0 <= x, y <= 99, and `x` and `y` are now assigned the values provided by the user input. If both `x` and `y` are greater than 0, `x` is updated to `x - math.ceil(y / 2) * 15 + y * 4`, and `bxsfory1` is set to `math.ceil(x / 15) + 1` if `x` is greater than 0, otherwise `bxsfory1` is 0. If either `x` is 0 or `y` is 0, no changes are made to `x` and `y`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads two non-negative integers `x` and `y` from user input, where both `x` and `y` are between 0 and 99 inclusive. The function then prints an integer based on the following conditions:
- If both `x` and `y` are greater than 0, it prints the sum of `math.ceil(y / 2)` and `math.ceil((x - math.ceil(y / 2) * 15 + y * 4) / 15) + 1` if the updated `x` is greater than 0, otherwise it prints `math.ceil(y / 2)`.
- If `x` is 0 and `y` is greater than 0, it prints `math.ceil(y / 2)`.
- If `x` is greater than 0 and `y` is 0, it prints `math.ceil(x / 15)`.
- If both `x` and `y` are 0, it prints 0.

#State of the program right berfore the function call: t is a non-negative integer such that 1 <= t <= 10^4.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: The value of `t` remains unchanged, and the loop has executed the function `func_2` `t` times.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a non-negative integer `t` (1 <= t <= 10^4) from user input and executes the function `func_2` `t` times. After the function concludes, the value of `t` remains unchanged. The function itself does not return any value.

