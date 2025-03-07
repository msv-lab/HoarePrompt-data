#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, x and y are integers where 0 ≤ x, y ≤ 99.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `x` and `y` are integers provided by the user input, `ap` is 0, `k` is `ap` (which is 0), `bxsfory` is the ceiling of the last `y / 2` processed, and `bxsfory1` is 0 if the last `x` is less than or equal to 0, otherwise `bxsfory1` is the ceiling of the last `x / 15`. If `x > 0` and `y > 0`, `x` is updated to `x - bxsfory * 15 + y * 4`. If `x == 0` and `y > 0`, or if `x > 0` and `y == 0`, or in any other case where `x` and `y` do not satisfy `x > 0` and `y > 0`, the values of `x`, `y`, `ap`, `k`, `bxsfory`, and `bxsfory1` remain unchanged.
#Overall this is what the function does:The function `func_1` processes a series of test cases. It reads an integer `ap` which specifies the number of test cases. For each test case, it reads two integers `x` and `y`. Depending on the values of `x` and `y`, it calculates and prints a result based on specific conditions: if both `x` and `y` are greater than 0, it computes a modified value of `x` and prints a combined result; if only `y` is greater than 0, it prints the ceiling of `y / 2`; if only `x` is greater than 0, it prints the ceiling of `x / 15`; otherwise, it prints 0. After processing all test cases, the function has no return value, and the state of the program includes the processed inputs and printed results.

