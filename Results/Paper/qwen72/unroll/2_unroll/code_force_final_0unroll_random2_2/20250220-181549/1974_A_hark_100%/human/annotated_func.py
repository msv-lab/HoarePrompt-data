#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x, y <= 99.
def func_1():
    ap = int(input())
    for k in range(ap):
        x, y = map(int, input().split())
        
        if x > 0 and y > 0:
            bxsfory = math.ceil(y / 2)
            x = x - bxsfory * 15 + y * 4
            bxsfory1 = 0 if x <= 0 else math.ceil(x / 15)
            print(bxsfory1 + bxsfory)
        elif x == 0 and y > 0:
            print(math.ceil(y / 2))
        elif x > 0 and y == 0:
            print(math.ceil(x / 15))
        else:
            print(0)
        
    #State: The values of `x` and `y` are updated based on the input provided during each iteration of the loop. The value of `ap` remains unchanged. The loop prints a value for each iteration, which is the sum of `bxsfory` and `bxsfory1` if both `x` and `y` are greater than 0, `math.ceil(y / 2)` if `x` is 0 and `y` is greater than 0, `math.ceil(x / 15)` if `x` is greater than 0 and `y` is 0, and 0 if both `x` and `y` are 0. After all iterations, the final values of `x` and `y` depend on the last input provided.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer `ap` from the user, which specifies the number of iterations. For each iteration, it reads two non-negative integers `x` and `y` from the user. Depending on the values of `x` and `y`, it calculates and prints a value based on the following rules: if both `x` and `y` are greater than 0, it prints the sum of `math.ceil(y / 2)` and `math.ceil((x - math.ceil(y / 2) * 15 + y * 4) / 15)` (if the result is positive); if `x` is 0 and `y` is greater than 0, it prints `math.ceil(y / 2)`; if `x` is greater than 0 and `y` is 0, it prints `math.ceil(x / 15)`; if both `x` and `y` are 0, it prints 0. The values of `x` and `y` are updated in each iteration, but their final state depends on the last input provided. The value of `ap` remains unchanged throughout the function.

