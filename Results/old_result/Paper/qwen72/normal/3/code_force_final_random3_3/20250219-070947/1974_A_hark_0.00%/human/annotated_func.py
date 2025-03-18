#State of the program right berfore the function call: a and b are values of any type that can be compared using the less than (<) operator.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller value between `a` and `b`. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`.
#Overall this is what the function does:The function `func_1` accepts two parameters, `a` and `b`, which are values of any type that can be compared using the less than (<) operator. It returns the smaller value between `a` and `b`. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`. After the function concludes, the program state is such that the returned value is the minimum of the two input values.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x, y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + bxsfory (where bxsfory is the ceiling of y / 2 and bxsfory1 is 0 if the updated x is less than or equal to 0, otherwise math.ceil(x / 15) + 1)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: (y + 1) // 2 if y is odd, y // 2 if y is even (where y is a non-negative integer greater than 0 and less than or equal to 99)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is a non-negative integer between 1 and 99, and the result is an integer between 1 and 7)
            else :
                print(0)
                #This is printed: 0
            #State: x and y are non-negative integers such that 0 <= x, y <= 99, and x, y are now assigned new values from user input. If x > 0 and y == 0, then the current value of x is greater than 0, and the current value of y is 0. Otherwise, it is not the case that (x > 0 and y == 0), and either x is 0 or y is 0, with the condition that it is not the case that (x == 0 and y > 0).
        #State: x and y are non-negative integers such that 0 <= x, y <= 99, and x, y are now assigned new values from user input. If x == 0 and y > 0, the current value of x is 0, and the current value of y is greater than 0. If x > 0 and y == 0, the current value of x is greater than 0, and the current value of y is 0. Otherwise, either x is 0 or y is 0, but it is not the case that (x == 0 and y > 0).
    #State: *x and y are non-negative integers such that 0 <= x, y <= 99. If x > 0 and y > 0, `x` is updated to `x - math.ceil(y / 2) * 15 + y * 4`, and `bxsfory1` is `math.ceil(x / 15) + 1` if `x` is greater than 0, otherwise `bxsfory1` is 0. If x == 0 and y > 0, the current value of x is 0, and the current value of y is greater than 0. If x > 0 and y == 0, the current value of x is greater than 0, and the current value of y is 0. If x == 0 and y == 0, both x and y remain 0.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads two non-negative integers, `x` and `y`, from user input, where both `x` and `y` are in the range 0 to 99. The function then prints a value based on the following conditions:
- If both `x` and `y` are greater than 0, it calculates `bxsfory` as the ceiling of `y / 2`, updates `x` to `x - bxsfory * 15 + y * 4`, and calculates `bxsfory1` as 0 if the updated `x` is less than or equal to 0, otherwise as the ceiling of the updated `x / 15` plus 1. It then prints the sum of `bxsfory` and `bxsfory1`.
- If `x` is 0 and `y` is greater than 0, it prints the ceiling of `y / 2`.
- If `x` is greater than 0 and `y` is 0, it prints the ceiling of `x / 15`.
- If both `x` and `y` are 0, it prints 0.

#State of the program right berfore the function call: t is a non-negative integer such that 1 <= t <= 10^4.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: The loop has executed `t` times, and `func_2()` has been called `t` times.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads an integer `t` from the user input, where `1 <= t <= 10^4`. It then calls the function `func_2` exactly `t` times. After the function concludes, `func_2` has been called `t` times, and the program state reflects that the loop has completed `t` iterations.

