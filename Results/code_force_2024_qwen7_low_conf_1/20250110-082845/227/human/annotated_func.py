#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and each test case consists of two space-separated integers x and y such that 0 ≤ x, y ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        x, y = map(int, input().split())
        
        print(min(x, y), max(x, y))
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 100\); `i` is `t`; for each iteration \(i\) from 1 to \(t\), `x` is an input integer, `y` is an input integer, the minimum of `x` and `y` is printed followed by the maximum of `x` and `y`.
#Overall this is what the function does:The function processes up to 100 test cases, each containing two integers \(x\) and \(y\) where \(0 \leq x, y \leq 9\). For each test case, it prints the minimum of \(x\) and \(y\) followed by the maximum of \(x\) and \(y\). After executing the function, the state of the program includes no further test cases to process, and the console output contains the minimum and maximum values for each pair of integers from the test cases.

