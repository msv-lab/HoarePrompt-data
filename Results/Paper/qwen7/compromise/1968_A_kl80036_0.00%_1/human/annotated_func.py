#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: Output State: The output state will consist of a series of integers printed, where each integer is half of the corresponding input integer \(x\) for each test case. Specifically, if there are \(t\) test cases, the output will be a list of \(t\) integers, each being the result of \(x_i // 2\) for \(i\) from 1 to \(t\).
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads an integer \(x\) (with \(2 \leq x \leq 1000\)) and prints half of \(x\) (\(x // 2\)). After processing all test cases, it outputs a list of integers, each being half of the corresponding input integer \(x\).

