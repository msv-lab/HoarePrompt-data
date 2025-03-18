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
        
    #State: The values of `x` and `y` are updated based on the input provided in each iteration of the loop. The variable `ap` remains unchanged.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer `ap` from the user, which determines the number of iterations. In each iteration, it reads two non-negative integers `x` and `y` (0 <= x, y <= 99) from the user. Depending on the values of `x` and `y`, it calculates and prints a value. If both `x` and `y` are greater than 0, it performs a calculation involving `x` and `y` and prints the result. If `x` is 0 and `y` is greater than 0, it prints the ceiling of `y / 2`. If `x` is greater than 0 and `y` is 0, it prints the ceiling of `x / 15`. If both `x` and `y` are 0, it prints 0. The function does not return any value. After the function concludes, the variable `ap` remains unchanged, and the values of `x` and `y` are updated in each iteration but are not retained outside the loop.

