#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case consists of two integers x and y (0 ≤ x, y ≤ 99), where x is the number of applications with a 1 × 1 icon and y is the number of applications with a 2 × 2 icon.
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
        
    #State: The output state consists of `t` lines, each representing the number of 3x5 screens required for the applications in each test case. The variables `x` and `y` are reset to the input values for each test case, and `ap` is the number of test cases processed. The state of `t` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of 1x1 and 2x2 applications, and calculates the minimum number of 3x5 screens required to display all applications in each test case.

