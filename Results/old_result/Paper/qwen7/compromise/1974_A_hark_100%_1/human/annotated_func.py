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
        
    #State: Output State: The output state will be a list of integers, each representing the value printed during each iteration of the loop based on the input values provided for `x` and `y`. The length of this list will be equal to the value of `ap`, and each element in the list will be calculated according to the conditions specified in the loop body. If `x` and `y` are both positive, the value will be the sum of `bxsfory` and `bxsfory1`. If `x` is zero and `y` is positive, the value will be `math.ceil(y / 2)`. If `x` is positive and `y` is zero, the value will be `math.ceil(x / 15)`. If both `x` and `y` are non-positive, the value will be `0`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two non-negative integers \(x\) and \(y\). For each test case, it calculates a value based on the given conditions: if both \(x\) and \(y\) are positive, it computes the sum of two ceiling values; if only \(y\) is positive, it computes the ceiling of \(y/2\); if only \(x\) is positive, it computes the ceiling of \(x/15\); and if both \(x\) and \(y\) are non-positive, it returns 0. The function outputs a list of these calculated values, one for each test case.

