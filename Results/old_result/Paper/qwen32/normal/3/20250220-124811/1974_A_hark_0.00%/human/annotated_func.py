#State of the program right berfore the function call: a and b are integers.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller of the two integers, a or b.
#Overall this is what the function does:The function accepts two integer parameters, `a` and `b`, and returns the smaller of the two integers.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x <= 99 and 0 <= y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: `math.ceil(y / 2)` if `x <= 0` after the update, otherwise `math.ceil(x / 15) + 1 + math.ceil(y / 2)`
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is a given integer greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is an integer between 1 and 99)
            else :
                print(0)
                #This is printed: 0
            #State: `x` and `y` are non-negative integers such that `0 <= x <= 99` and `0 <= y <= 99`. If `x` is greater than 0 and `y` is 0, the condition holds. Otherwise, either `x` is 0 and `y` is 0, or `x` is 0 and `y` is not 0, or `x` is not 0 and `y` is not 0.
        #State: `x` and `y` are non-negative integers such that `0 <= x <= 99` and `0 <= y <= 99`. If `x` is 0 and `y` is greater than 0, the condition holds. If `x` is greater than 0 and `y` is 0, the condition holds. Otherwise, either `x` is 0 and `y` is 0, or `x` is not 0 and `y` is not 0.
    #State: `x` and `y` are non-negative integers such that `0 <= x <= 99` and `0 <= y <= 99`. If both `x` and `y` are greater than 0, `x` is updated to `x - math.ceil(y / 2) * 15 + y * 4`, `y` remains unchanged, `bxsfory` is set to `math.ceil(y / 2)`, and `bxsfory1` is `0 if x <= 0 else math.ceil(x / 15) + 1`. If either `x` or `y` (or both) is 0, `x` and `y` retain their original values.
#Overall this is what the function does:The function reads two non-negative integers `x` and `y` (where `0 <= x <= 99` and `0 <= y <= 99`) from the input, performs calculations based on their values, and prints a result. The printed result is the sum of `math.ceil(y / 2)` and `math.ceil(x / 15) + 1` if both `x` and `y` are greater than 0, `math.ceil(y / 2)` if `x` is 0 and `y` is greater than 0, `math.ceil(x / 15)` if `x` is greater than 0 and `y` is 0, and `0` if both `x` and `y` are 0.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `t` remains the input integer, such that 1 <= t <= 10^4.
#Overall this is what the function does:The function `func_3` reads a positive integer `t` from the input, where `1 <= t <= 10^4`, and calls `func_2` `t` times. It does not return any value.

