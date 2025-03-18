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
        
    #State: Output State: The output will consist of multiple lines where each line starts with a space followed by '1' repeated `n` times, where `n` is an integer input provided during each iteration of the loop. This process repeats until `t` becomes 0.
    #
    #To provide a concrete example, if `t` is set to 3 initially:
    #
    #1. For the first iteration (`t = 3`), the user inputs an integer `n`. Let's say `n` is 4. The output will be:
    #   ```
    #     1 1 1 1 
    #   ```
    #
    #2. For the second iteration (`t = 2`), if another `n` is 5, the output will be:
    #   ```
    #     1 1 1 1 1 
    #   ```
    #
    #3. For the third iteration (`t = 1`), if `n` is 3, the output will be:
    #   ```
    #     1 1 1 
    #   ```
    #
    #After all iterations, the final output will look like the concatenation of these lines, each separated by a newline, starting with a space on the first line as per the loop's print statement.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( t \) and \( n \) from the input, where \( 1 \leq t \leq 50 \) and \( 2 \leq n \leq 10^3 \). It then prints \( n \) occurrences of the number 1 on each of \( t \) lines, with each line starting with a space. After processing all test cases, it ends without returning any value.

