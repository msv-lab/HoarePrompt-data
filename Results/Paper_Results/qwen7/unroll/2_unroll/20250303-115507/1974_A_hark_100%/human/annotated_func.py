#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
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
        
    #State: Output State: The output state will consist of a series of integers printed during each iteration of the loop. For each iteration, the value printed depends on the inputs `x` and `y` provided by the `input().split()` function. If both `x` and `y` are positive, the output is calculated based on the formulas involving ceiling functions and arithmetic operations with `x` and `y`. If only one of them is positive, the output is either the ceiling of `y/2` or `x/15`, depending on which variable is positive. If both are zero, the output is 0. The exact sequence of outputs will depend on the specific values of `x` and `y` entered during each iteration.
#Overall this is what the function does:The function processes a series of test cases (up to 10,000). For each test case, it reads two integers \(x\) and \(y\) (both between 0 and 99). Based on the values of \(x\) and \(y\), it calculates and prints one of the following:
- The sum of \(\left\lceil \frac{y}{2} \right\rceil\) and \(\left\lceil \frac{x - \left\lceil \frac{y}{2} \right\rceil \times 15 + y \times 4}{15} \right\rceil\) if both \(x\) and \(y\) are positive.
- \(\left\lceil \frac{y}{2} \right\rceil\) if only \(y\) is positive.
- \(\left\lceil \frac{x}{15} \right\rceil\) if only \(x\) is positive.
- 0 if both \(x\) and \(y\) are zero.

