#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, m such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: Output State: The output state will consist of a series of integers, each representing the result of the expression `m // a + m // b + 2` for each iteration of the loop, where `a`, `b`, and `m` are provided by user input for each iteration. The number of integers in the output state will be equal to the value of `t`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(m\) provided by user input. For each test case, it calculates the value of \(m // a + m // b + 2\) and prints the result. The function reads the number of test cases \(t\) first, then iterates through each test case, performing the calculation and outputting the result. The final state of the program is a series of integers printed to the console, each corresponding to the calculated value for each test case.

