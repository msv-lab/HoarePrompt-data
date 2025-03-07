#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are non-negative integers such that 0 ≤ x, y ≤ 99.
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
        
    #State: The loop has executed all its iterations, and the final state of the variables is as follows: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `ap` is a positive integer, and `k` is equal to `ap`. The values of `x` and `y` are the result of applying the operations within the loop for each iteration specified by `ap`. Specifically, for each iteration, if `x > 0` and `y > 0`, `x` is updated to `x - bxsfory * 15 + y * 4`, where `bxsfory` is the ceiling value of `y / 2`, and `bxsfory1` is 0 if `x - bxsfory * 15 + y * 4` is less than or equal to 0, else `bxsfory1` is the ceiling value of `(x - bxsfory * 15 + y * 4) / 15`. If either `x` or `y` is not greater than 0, `x` remains the first integer input from the user and `y` remains the second integer input from the user.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` (1 ≤ t ≤ 10^4) and pairs of non-negative integers `x` and `y` (0 ≤ x, y ≤ 99). For each test case, it calculates and prints a value based on the given inputs. If both `x` and `y` are greater than 0, it updates `x` according to specific rules and then calculates and prints a sum involving `x` and `y`. If only `y` is greater than 0, it calculates and prints a value based on `y`. If only `x` is greater than 0, it calculates and prints a value based on `x`. If neither `x` nor `y` is greater than 0, it prints 0.

