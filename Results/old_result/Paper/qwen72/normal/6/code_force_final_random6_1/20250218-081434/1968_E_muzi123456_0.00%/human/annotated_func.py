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
        
    #State: `t` is 0, `n` is an input integer such that 2 <= n <= 10^3, `i` is `n`.
#Overall this is what the function does:The function `func` accepts no parameters and reads input from the user. It processes `t` test cases, where `t` is an integer between 1 and 50. For each test case, it reads an integer `n` (2 <= n <= 10^3) and prints a sequence of lines. Each line consists of the string '1' followed by an integer from 1 to `n`. After processing all test cases, the function ensures that `t` is 0, and the final state of the program is such that all test cases have been processed and the corresponding sequences have been printed.

