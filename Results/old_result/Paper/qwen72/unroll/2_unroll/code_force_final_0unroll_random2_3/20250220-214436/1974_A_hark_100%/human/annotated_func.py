#State of the program right berfore the function call: The function should take two non-negative integers x and y as input, where 0 <= x, y <= 99, representing the number of 1x1 and 2x2 icons respectively.
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
        
    #State: The values of `x` and `y` are unchanged, and `ap` remains the same.
#Overall this is what the function does:The function `func_1` reads an integer `ap` from the user, representing the number of test cases. For each test case, it reads two non-negative integers `x` and `y` from the user, representing the number of 1x1 and 2x2 icons respectively. It calculates and prints the minimum number of boxes required to store these icons, where each box can hold 15 1x1 icons or 2 2x2 icons. The function does not return any value and does not modify the input variables `x` and `y`. After the function concludes, the values of `x` and `y` are unchanged, and `ap` remains the same.

