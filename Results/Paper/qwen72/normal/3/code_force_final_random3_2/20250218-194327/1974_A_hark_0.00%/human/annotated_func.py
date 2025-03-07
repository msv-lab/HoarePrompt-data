#State of the program right berfore the function call: a and b are values of any type that can be compared.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller value between `a` and `b` if `a` is less than `b`; otherwise, it returns `b`.
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, which are values of any type that can be compared. It returns the smaller of the two values. If `a` is less than `b`, it returns `a`; otherwise, it returns `b`.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x, y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + bxsfory (where bxsfory is math.ceil(y / 2) and bxsfory1 is 0 if x is less than or equal to 0, otherwise math.ceil(x / 15) + 1)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: (y + 1) // 2 (where y is a non-negative integer greater than 0 and less than or equal to 99)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is a non-negative integer greater than 0 and less than or equal to 99, and the result is an integer between 1 and 7 inclusive)
            else :
                print(0)
                #This is printed: 0
            #State: *x and y are non-negative integers such that 0 <= x, y <= 99, and x, y are assigned the values from the input. If x > 0 and y == 0, then x is greater than 0 and y is 0. Otherwise, either x is 0, or y is not 0.
        #State: x and y are non-negative integers such that 0 <= x, y <= 99, and x, y are assigned the values from the input. If x is 0 and y is greater than 0, the current value of x is 0, and the current value of y is greater than 0. If x is greater than 0 and y is 0, then x is greater than 0 and y is 0. Otherwise, either x is 0, or y is not 0.
    #State: *x and y are non-negative integers such that 0 <= x, y <= 99. If `x > 0` and `y > 0`, `x` is updated to `x - math.ceil(y / 2) * 15 + y * 4`, `y` is a non-negative integer such that 0 < y <= 99, `bxsfory` is equal to `math.ceil(y / 2)`, and `bxsfory1` is 0 if `x` is less than or equal to 0, otherwise `bxsfory1` is `math.ceil(x / 15) + 1`. If `x` is 0 and `y` is greater than 0, the current value of `x` is 0, and the current value of `y` is greater than 0. If `x` is greater than 0 and `y` is 0, then `x` is greater than 0 and `y` is 0. Otherwise, either `x` is 0, or `y` is not 0.
#Overall this is what the function does:The function `func_2` does not accept any parameters and reads two non-negative integers `x` and `y` from user input, where both `x` and `y` are in the range 0 to 99. It then prints a result based on the values of `x` and `y`:
- If both `x` and `y` are greater than 0, it prints the sum of `math.ceil(y / 2)` and `math.ceil((x - math.ceil(y / 2) * 15 + y * 4) / 15) + 1` if the updated `x` is greater than 0, otherwise it prints `math.ceil(y / 2)`.
- If `x` is 0 and `y` is greater than 0, it prints `math.ceil(y / 2)`.
- If `x` is greater than 0 and `y` is 0, it prints `math.ceil(x / 15)`.
- If both `x` and `y` are 0, it prints 0.

#State of the program right berfore the function call: t is a non-negative integer such that 1 <= t <= 10^4.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `t` must be greater than or equal to 1, `func_2()` has been called `t` times.
#Overall this is what the function does:The function `func_3` reads a non-negative integer `t` from user input, where `1 <= t <= 10^4`, and calls the function `func_2` exactly `t` times. After the function concludes, `t` remains a non-negative integer greater than or equal to 1, and `func_2` has been executed `t` times. The function does not return any value.

