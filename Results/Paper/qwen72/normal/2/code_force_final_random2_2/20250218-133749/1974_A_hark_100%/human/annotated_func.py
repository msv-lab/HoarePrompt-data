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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `x` and `y` are integers read from input, `ap` is 0, `k` is `ap` (which is 0). For each iteration, if `x > 0` and `y > 0`, `x` was updated to `x - (ceiling(y / 2) * 15) + (y * 4)` and `y` remained greater than 0. The value of `bxsfory` was `math.ceil(y / 2)`, and `bxsfory1` was 0 if the new `x` was less than or equal to 0, otherwise `bxsfory1` was `math.ceil(new_x / 15)`. If `x` == 0 and `y` > 0, the value printed was `math.ceil(y / 2)`. If `x` > 0 and `y` == 0, the value printed was `math.ceil(x / 15)`. In all other cases, the value printed was 0. After all iterations, `ap` is 0, and `k` has reached the final value of `ap` (which is 0).
#Overall this is what the function does:The function `func_1` reads an integer `ap` from the input, which represents the number of test cases. For each test case, it reads two integers `x` and `y` from the input. Depending on the values of `x` and `y`, it calculates and prints a result based on the following rules: 
- If both `x` and `y` are greater than 0, it computes a modified value of `x` and prints the sum of two ceiling divisions.
- If `x` is 0 and `y` is greater than 0, it prints the ceiling division of `y` by 2.
- If `x` is greater than 0 and `y` is 0, it prints the ceiling division of `x` by 15.
- If both `x` and `y` are 0, it prints 0.
After processing all test cases, the function ends, and the variable `ap` is 0.

