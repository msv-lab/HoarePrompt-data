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
        
    #State: `t` is 0, `n` is an input integer greater than or equal to 2, `i` is `n`.
#Overall this is what the function does:The function reads an integer `t` (1 to 50) representing the number of test cases. For each test case, it reads an integer `n` (2 to 1000) and prints a sequence of numbers. Specifically, for each `n`, it prints '1' followed by each integer from 1 to `n` on separate lines. After processing all test cases, `t` is 0, and the function has no return value.

