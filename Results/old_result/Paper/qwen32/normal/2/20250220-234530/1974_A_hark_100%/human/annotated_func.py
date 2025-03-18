#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, there are two integers x and y such that 0 ≤ x, y ≤ 99.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `ap` is an integer greater than 0, and `x` and `y` are the last pair of integers read from the input during the last iteration of the loop.
#Overall this is what the function does:The function reads an integer `ap` representing the number of test cases. For each test case, it reads two integers `x` and `y`. It then calculates and prints a value based on the following rules: if both `x` and `y` are greater than 0, it computes a specific formula involving `x` and `y` and prints the result; if only `y` is greater than 0, it prints half of `y` rounded up; if only `x` is greater than 0, it prints `x` divided by 15 rounded up; if both `x` and `y` are 0, it prints 0.

