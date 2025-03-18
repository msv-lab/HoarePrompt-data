#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: Output State: The output will consist of `t` blocks, each block containing a sequence of lines. Each block starts with a line printing '1' followed by a space-separated list of numbers from 1 to `n`, where `n` is the input provided during that iteration. After each block, there is an additional empty line.
    #
    #To be more specific, if `t` is 3, the output might look like this:
    #
    #```
    #1 1 
    #1 2 
    #
    #1 1 
    #1 2 
    #1 3 
    #
    #1 1 
    #1 2 
    #1 3 
    #1 4 
    #```
    #
    #Each block corresponds to one decrement of `t`. The value of `n` is determined by user input during each iteration, and it changes with each input.
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer between 1 and 50. For each test case, it reads an integer `n` (between 2 and 10^3) and prints a block of output. Each block consists of `n` lines, starting with '1' followed by the numbers from 1 to `n` separated by spaces. After each block, an empty line is printed. The function does not return any value.

