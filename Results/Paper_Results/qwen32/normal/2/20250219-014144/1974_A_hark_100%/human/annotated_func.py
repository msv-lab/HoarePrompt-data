#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, there are two integers x and y such that 0 ≤ x, y ≤ 99.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, and `ap` is an integer representing the number of iterations which has been fully executed. No further changes to `x` and `y` as they are re-read for each iteration.
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y`. It then calculates and prints a value based on the conditions involving `x` and `y`. Specifically, it computes the minimum number of operations needed to reduce `x` and `y` to zero using specific rules, and prints this value for each test case.

