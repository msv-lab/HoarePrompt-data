#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: For each of the `t` test cases, there will be `n` lines of output, each containing '1' followed by the line number (from 1 to `n`). After each test case's output, there is an additional blank line. The value of `t` will be 0, and `n` will be the last integer input for the final test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads an integer `n`. It then prints `n` lines, each containing the number `1` followed by the line number (from 1 to `n`). After each test case's output, it prints a blank line.

