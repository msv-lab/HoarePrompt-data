#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: Output State: The output will consist of multiple lines, each corresponding to one iteration of the while loop. For each iteration, there will be `n` lines printed, where the first line prints "1" followed by the number `i` (for `i` from 1 to `n`), and the second line prints a space. This process repeats `t` times, with `t` being the initial value provided as input.
    #
    #For example, if `t` is 2 and `n` is 3 during the first iteration and 4 during the second iteration, the output would look like:
    #
    #```
    #1 1 
    # 1 2 
    # 1 3 
    #
    # 1 1 
    # 1 2 
    # 1 3 
    # 1 4 
    #```
    #
    #This pattern continues until the while loop has executed `t` times.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of two integers: `t` (number of iterations, 1 ≤ t ≤ 50) and `n` (a value used in a loop, 2 ≤ n ≤ 10^3). For each test case, it prints `t` blocks, each block containing `n` lines. Each line in a block starts with '1' followed by a number from 1 to `n`, with a space between them. After printing each block, it prints a newline.

