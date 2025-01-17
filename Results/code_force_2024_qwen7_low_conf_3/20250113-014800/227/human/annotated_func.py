#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        x, y = map(int, input().split())
        
        print(min(x, y), max(x, y))
        
    #State of the program after the  for loop has been executed: `t` is an integer equal to the input provided by the user, and 1 ≤ `t` ≤ 100, `i` is `t`, the print function has executed `t` times displaying the minimum and maximum of `x` and `y` for each pair of inputs.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \(x\) and \(y\). For each test case, it prints the minimum and maximum values of \(x\) and \(y\). The function reads an integer \(t\) representing the number of test cases, where \(1 \leq t \leq 100\). After processing all test cases, the function concludes with no return value. Potential edge cases include \(t = 1\) (only one test case) and \(t = 100\) (maximum number of test cases). The function also handles invalid inputs by ensuring \(0 \leq x, y \leq 9\) within each test case. However, the function does not explicitly handle cases where \(x\) or \(y\) are outside this range, which could result in incorrect output.

