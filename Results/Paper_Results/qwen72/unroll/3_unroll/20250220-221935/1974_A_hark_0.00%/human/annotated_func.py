#State of the program right berfore the function call: a and b are values of any type that support comparison.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller value between `a` and `b`. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`.
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, which are values of any type that support comparison, and returns the smaller of the two values. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`. After the function concludes, the program has the smaller value between `a` and `b` available for further use.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x, y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: - The exact value of the sum will depend on the specific values of `x` and `y`, but we can describe the range of possible values.
        #
        #Output:
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is a positive integer between 1 and 99)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is a non-negative integer greater than 0 and less than or equal to 99, and the result is an integer between 1 and 7)
            else :
                print(0)
                #This is printed: 0
            #State: *x and y are non-negative integers such that 0 <= x, y <= 99, x and y are assigned the values from the input. If x > 0 and y == 0, no changes are made. If x is 0 or y is not 0, no changes are made.
        #State: *x and y are non-negative integers such that 0 <= x, y <= 99, x and y are assigned the values from the input. If x is 0 and y is greater than 0, no changes are made. If x is greater than 0 and y is 0, no changes are made. If x is 0 and y is 0, no changes are made. If x is greater than 0 and y is greater than 0, no changes are made.
    #State: *`x` and `y` are non-negative integers such that 0 <= x, y <= 99, and they are assigned the values from the input. If `x` > 0 and `y` > 0, `bxsfory` is equal to `math.ceil(y / 2)`, and `bxsfory1` is `math.ceil(x / 15) + 1`. If either `x` is 0 or `y` is 0, no changes are made to `x` and `y`, and `bxsfory` and `bxsfory1` remain unchanged.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads two non-negative integers `x` and `y` from the user input, where 0 <= x, y <= 99. Based on the values of `x` and `y`, it prints a calculated value. If both `x` and `y` are greater than 0, it prints the sum of `math.ceil(y / 2)` and `math.ceil((x - math.ceil(y / 2) * 15 + y * 4) / 15) + 1`. If `x` is 0 and `y` is greater than 0, it prints `math.ceil(y / 2)`. If `x` is greater than 0 and `y` is 0, it prints `math.ceil(x / 15)`. If both `x` and `y` are 0, it prints 0. The function does not return any value.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: The value of `t` remains unchanged, and `func_2` has been called `t` times.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads an integer `t` from the user input where `1 <= t <= 10^4`. The function then calls `func_2` exactly `t` times. After the function concludes, the value of `t` remains unchanged, and `func_2` has been called `t` times. The function does not return any value.

