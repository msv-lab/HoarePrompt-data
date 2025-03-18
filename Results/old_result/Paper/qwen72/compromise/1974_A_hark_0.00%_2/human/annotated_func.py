#State of the program right berfore the function call: a and b are values of any type that can be compared using the less than (<) operator.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller value between `a` and `b`. If `a` is less than `b`, it returns `a`. Otherwise, it returns `b`.
#Overall this is what the function does:The function `func_1` accepts two parameters, `a` and `b`, which are values of any type that can be compared using the less than (<) operator. It returns the smaller value between `a` and `b`. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`. The function does not modify the input parameters.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x, y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + bxsfory (where bxsfory is the ceiling of y divided by 2, and bxsfory1 is 0 if the updated x is less than or equal to 0, otherwise it is math.ceil(x / 15) + 1)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is a positive integer greater than 0 and less than or equal to 99)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: - The `print` statement will output the ceiling of \(x / 15\), which is an integer between 1 and 7.
                #
                #Output:
            else :
                print(0)
                #This is printed: 0
            #State: *`x` and `y` are non-negative integers such that 0 <= x, y <= 99, and `x` and `y` are now assigned the values from the input. If `x` is greater than 0 and `y` is 0, the conditions remain unchanged. Otherwise, either `x` is 0, or `y` is not 0, or both, and the conditions remain unchanged.
        #State: *`x` and `y` are non-negative integers such that 0 <= x, y <= 99, and `x` and `y` are now assigned the values from the input. If `x` is 0 and `y` is a positive integer greater than 0, the conditions remain unchanged. If `x` is greater than 0 and `y` is 0, the conditions also remain unchanged. Otherwise, either `x` is 0, or `y` is not 0, or both, and the conditions remain unchanged.
    #State: *`x` and `y` are non-negative integers such that 0 <= x, y <= 99. If `x` > 0 and `y` > 0, `x` is updated to `x - bxsfory * 15 + y * 4`, where `bxsfory` is the ceiling of `y` divided by 2, and `bxsfory1` is 0 if the updated `x` is less than or equal to 0, otherwise `bxsfory1` is `math.ceil(x / 15) + 1`. If `x` is 0 or `y` is 0 (or both), `x` and `y` retain their original values from the input.
#Overall this is what the function does:The function `func_2` reads two non-negative integers `x` and `y` from user input, where both `x` and `y` are in the range 0 to 99. It then prints a value based on the following conditions: If both `x` and `y` are greater than 0, it prints the sum of the ceiling of `y / 2` and a calculated value based on the updated `x`. If `x` is 0 and `y` is greater than 0, it prints the ceiling of `y / 2`. If `x` is greater than 0 and `y` is 0, it prints the ceiling of `x / 15`. If both `x` and `y` are 0, it prints 0. The function does not return any value.

#State of the program right berfore the function call: t is a non-negative integer such that 1 <= t <= 10^4.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: The value of `t` remains unchanged, and `func_2()` has been called `t` times.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a non-negative integer `t` from the user input where 1 <= t <= 10^4. It then calls the function `func_2` exactly `t` times. After the function concludes, the value of `t` remains unchanged, and `func_2` has been called `t` times.

