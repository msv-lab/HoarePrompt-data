#State of the program right berfore the function call: a and b are non-negative integers.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller of the two non-negative integers `a` and `b`.
#Overall this is what the function does:The function accepts two non-negative integers `a` and `b`, and returns the smaller of the two integers.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x <= 99 and 0 <= y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: 11 (where bxsfory is math.ceil(y / 2) and bxsfory1 is 0 if x <= 0 else math.ceil(x / 15) + 1, with x calculated as x_initial - bxsfory * 15 + y * 4)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is an integer greater than 0 and less than or equal to 99)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where math.ceil(x / 15) is the smallest integer greater than or equal to x / 15, and x is an integer between 1 and 99)
            else :
                print(0)
                #This is printed: 0
            #State: `x` and `y` are the two integers provided as input, where 0 <= x <= 99 and 0 <= y <= 99. If `x` is greater than 0 and `y` is 0, the conditions specified in the if part hold. Otherwise, either `x` is 0, or `y` is 0, or both are 0, and it is not the case that `x` is 0 and `y` is greater than 0. Additionally, it is not the case that `x` is greater than 0 and `y` is equal to 0.
        #State: `x` and `y` are the two integers provided as input, where 0 <= x <= 99 and 0 <= y <= 99. If `x` is 0 and `y` is greater than 0, the conditions specified in the if part hold. Otherwise, either `x` is 0, or `y` is 0, or both are 0, and it is not the case that `x` is 0 and `y` is greater than 0. Additionally, it is not the case that `x` is greater than 0 and `y` is equal to 0.
    #State: `x` and `y` are integers with initial values in the range 0 to 99. If both `x` and `y` are greater than 0, then `x` is updated to `x - bxsfory * 15 + y * 4` where `bxsfory` is the smallest integer greater than or equal to `y / 2`. If either `x` or `y` is 0 (or both are 0), the values of `x` and `y` remain unchanged. If `x` is 0 and `y` is greater than 0, the conditions specified in the if part hold.
#Overall this is what the function does:The function `func_2` reads two non-negative integers `x` and `y` from the input, where each is between 0 and 99 inclusive. It then calculates and prints a value based on the conditions: if both `x` and `y` are greater than 0, it computes a specific formula involving `x` and `y` and prints the result. If only `y` is greater than 0, it prints half of `y` rounded up. If only `x` is greater than 0, it prints `x` divided by 15 rounded up. If both `x` and `y` are 0, it prints 0.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `t` remains the integer value provided by the user, and `func_2()` has been executed `t` times.
#Overall this is what the function does:The function `func_3` reads a positive integer `t` from the user input, and then executes `func_2` exactly `t` times. The function does not accept any parameters and does not return any specific value.

