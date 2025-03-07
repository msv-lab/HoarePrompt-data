#State of the program right berfore the function call: a and b are integers.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller of the two integers a and b.
#Overall this is what the function does:The function accepts two integer parameters and returns the smaller of the two.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x <= 99 and 0 <= y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + bxsfory (where bxsfory is the ceiling of y / 2 and bxsfory1 is math.ceil(x / 15) + 1)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is a positive integer greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: an integer between 1 and 7 (inclusive), depending on the value of `x`
            else :
                print(0)
                #This is printed: 0
            #State: `x` and `y` are integers such that 0 <= `x` <= 99 and 0 <= `y` <= 99. If `x` is greater than 0 and `y` is 0, then the conditions remain as specified in the if part. Otherwise, at least one of `x` or `y` is 0, and it is not the case that `x` is 0 and `y` is greater than 0. It is also ensured that it is not the case that `x` is greater than 0 and `y` is 0.
        #State: `x` and `y` are integers within the range 0 <= `x` <= 99 and 0 <= `y` <= 99. If `x` is 0 and `y` is greater than 0, the conditions remain as specified. Otherwise, at least one of `x` or `y` is 0, and it is not the case that `x` is 0 and `y` is greater than 0. Additionally, it is ensured that it is not the case that both `x` and `y` are greater than 0.
    #State: `x` and `y` are integers within the range 0 <= `x` <= 99 and 0 <= `y` <= 99. If both `x` and `y` are greater than 0, then `x` is updated to `x - bxsfory * 15 + y * 4`, where `bxsfory` is the ceiling of `y / 2`. If `x` is 0 and `y` is greater than 0, the conditions remain as specified. Otherwise, at least one of `x` or `y` is 0, and it is not the case that `x` is 0 and `y` is greater than 0. Additionally, it is ensured that it is not the case that both `x` and `y` are greater than 0.
#Overall this is what the function does:The function `func_2` reads two non-negative integers `x` and `y` from the input, where `0 <= x <= 99` and `0 <= y <= 99`. It then calculates and prints a value based on the conditions: if both `x` and `y` are greater than 0, it computes a specific formula and prints the result; if only `y` is greater than 0, it prints the ceiling of `y / 2`; if only `x` is greater than 0, it prints the ceiling of `x / 15`; if both are 0, it prints 0.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 10^4\)
#Overall this is what the function does:The function reads a positive integer `t` from the input, which represents the number of times to execute `func_2()`. It then calls `func_2()` exactly `t` times. The function does not return any value.

