#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: `t` is an integer such that \(1 \leq t \leq 100\), `i` is 99 (since the loop runs `x` times and `x` can be any positive integer up to 100 based on the initial state), `x` is an input integer greater than 0, `y` is an integer obtained from the input split and converted to an integer, and after executing the if-else block 99 times, the final values of `x` and `y` will be the last pair of integers provided as input, with the condition that either `x` is less than `y` or `x` is greater than or equal to `y` remains unchanged. The variable `t` remains within its initial bounds, and `i` reaches its maximum possible value given the constraints of the problem.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \(x\) and \(y\) such that \(0 \leq x, y \leq 9\). For each test case, it prints the pair \(x, y\) if \(x < y\), otherwise it prints \(y, x\). After processing all test cases, it ensures that the output respects the given constraints and conditions.

