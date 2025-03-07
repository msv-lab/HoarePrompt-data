#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: Output State: The output state will consist of a series of integers printed, each being half of the corresponding input integer \(x\) for each test case. Specifically, for each test case, the value of \(y = x // 2\) will be printed. The number of such outputs will be equal to the number of test cases specified by the first input integer \(t\).
#Overall this is what the function does:The function reads a series of test cases, each consisting of a positive integer \(t\) and an integer \(x\). For each test case, it calculates \(y = x // 2\) and prints the value of \(y\). The function does not return any value but prints the results for each test case.

