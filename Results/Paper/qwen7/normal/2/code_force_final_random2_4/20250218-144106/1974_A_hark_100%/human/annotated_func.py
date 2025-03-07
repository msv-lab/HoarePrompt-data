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
        
    #State: After the loop executes all iterations, `t` is an integer such that 1 ≤ t ≤ 10^4, `ap` is an input integer, `k` is equal to `ap`, and `x` is updated according to the loop's logic for each iteration. Specifically, if `x > 0` and `y > 0`, `x` is updated to `x - bxsfory * 15 + y * 4`, where `bxsfory` is the ceiling value of `y / 2`. If `x <= 0`, `x` remains unchanged. If `x == 0` and `y > 0`, `x` remains unchanged. If `x > 0` and `y == 0`, `x` is updated to `math.ceil(x / 15)`. If neither condition is met, `x` remains unchanged. The value of `bxsfory1` is calculated as 0 if `x <= 0` else the ceiling value of `x / 15` if `x > 0` and `y > 0`. The value printed in each iteration is either `bxsfory1 + bxsfory` if both `x > 0` and `y > 0`, `math.ceil(y / 2)` if `x == 0` and `y > 0`, `math.ceil(x / 15)` if `x > 0` and `y == 0`, or `0` otherwise.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \(x\) and \(y\). For each test case, it calculates and prints a value based on the values of \(x\) and \(y\). If both \(x > 0\) and \(y > 0\), it calculates \(x\) as \(x - \text{ceil}(y / 2) \times 15 + y \times 4\) and prints \(\text{ceil}(x / 15) + \text{ceil}(y / 2)\). If \(x == 0\) and \(y > 0\), it prints \(\text{ceil}(y / 2)\). If \(x > 0\) and \(y == 0\), it prints \(\text{ceil}(x / 15)\). If neither condition is met, it prints \(0\). The function does not return any value but prints the result for each test case.

