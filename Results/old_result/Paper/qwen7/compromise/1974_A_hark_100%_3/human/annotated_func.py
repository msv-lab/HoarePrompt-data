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
        
    #State: Output State: The value of `t` remains unchanged, and for each iteration `k` from `0` to `ap-1`, the output is calculated based on the input values `x` and `y`. If both `x` and `y` are positive, the output is the sum of `bxsfory` and `bxsfory1`. If `x` is zero and `y` is positive, the output is `math.ceil(y / 2)`. If `x` is positive and `y` is zero, the output is `math.ceil(x / 15)`. If both `x` and `y` are non-positive, the output is `0`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two non-negative integers \(x\) and \(y\), and a positive integer \(t\) (1 ≤ \(t\) ≤ 10^4). For each test case, it calculates and outputs a value based on the following conditions:
- If both \(x\) and \(y\) are positive, it computes the sum of \(\text{math.ceil}(y / 2)\) and \(\text{math.ceil}(x / 15)\).
- If \(x\) is zero and \(y\) is positive, it outputs \(\text{math.ceil}(y / 2)\).
- If \(x\) is positive and \(y\) is zero, it outputs \(\text{math.ceil}(x / 15)\).
- If both \(x\) and \(y\) are non-positive, it outputs 0.
The function does not return a single value but prints the result for each test case individually.

