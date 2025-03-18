#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: Output State: The output state will consist of `t` lines, where each line contains the result of the expression `m // a + m // b + 2` for the corresponding input values of `a`, `b`, and `m` provided in the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(m\). For each test case, it calculates the value of \(m // a + m // b + 2\) and prints the result. The function reads the number of test cases \(t\) from the input first, then iterates through each test case, performing the calculation and outputting the result. After processing all test cases, the function concludes with the specified output state.

