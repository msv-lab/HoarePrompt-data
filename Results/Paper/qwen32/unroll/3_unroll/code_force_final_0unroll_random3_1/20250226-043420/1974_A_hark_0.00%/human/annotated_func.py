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
        #This is printed: `bxsfory1 + bxsfory` (where `bxsfory` is the ceiling of `y / 2` and `bxsfory1` is `0 if x <= 0 else math.ceil(x / 15) + 1`)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: - Since `y` is greater than 0 but we don't know its exact value, we can't determine a specific numerical output. However, we can describe it in terms of `y`.
            #   - The result of `y / 2` will be a positive number, and `math.ceil(y / 2)` will round this number up to the nearest integer.
            #
            #Given the above analysis, the output will be the ceiling value of `y / 2`.
            #
            #Output:
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is an integer such that 1 <= x <= 99)
            else :
                print(0)
                #This is printed: 0
            #State: `x` and `y` are integers obtained from the input, where `0 <= x <= 99` and `0 <= y <= 99`. If `x` is greater than 0 and `y` is 0, the conditions remain as they are. Otherwise, at least one of `x` or `y` is not greater than 0, and it is not the case that `x` is 0 and `y` is greater than 0. Additionally, it is not the case that `x` is greater than 0 and `y` is equal to 0.
        #State: `x` and `y` are integers obtained from the input, where `0 <= x <= 99` and `0 <= y <= 99`. If `x` equals 0 and `y` is greater than 0, the conditions remain as they are. Otherwise, at least one of `x` or `y` is not greater than 0, and it is not the case that `x` is 0 and `y` is greater than 0. Additionally, it is not the case that `x` is greater than 0 and `y` is equal to 0.
    #State: `x` and `y` are integers. If both `x` and `y` are greater than 0, then `x` is updated to `x - bxsfory * 15 + y * 4`, where `bxsfory` is the ceiling of `y / 2`. If either `x` or `y` is not greater than 0, or if `x` equals 0 and `y` is greater than 0, the values of `x` and `y` remain as they were obtained from the input, with `0 <= x <= 99` and `0 <= y <= 99`.
#Overall this is what the function does:The function `func_2` reads two non-negative integers `x` and `y` (where 0 <= x <= 99 and 0 <= y <= 99) from the input. It then calculates and prints a value based on the following conditions:
- If both `x` and `y` are greater than 0, it prints the sum of the ceiling of `y / 2` and the ceiling of the adjusted `x` value divided by 15, adjusted by `y * 4`.
- If `x` is 0 and `y` is greater than 0, it prints the ceiling of `y / 2`.
- If `x` is greater than 0 and `y` is 0, it prints the ceiling of `x / 15`.
- If both `x` and `y` are 0, it prints 0.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `t` remains unchanged as a positive integer such that 1 <= `t` <= 10^4.
#Overall this is what the function does:The function `func_3` reads an integer `t` from the input, which is a positive integer between 1 and 10,000 inclusive, and then calls `func_2` exactly `t` times. The function does not return any value.

