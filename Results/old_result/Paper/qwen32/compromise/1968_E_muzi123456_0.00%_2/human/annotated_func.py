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
        
    #State: t is 0, and for each of the initial t test cases, the numbers from 1 to n have been printed in the format '1 i' for each i from 1 to n, followed by a space.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints the numbers from 1 to `n` in the format '1 i' for each `i` from 1 to `n`, followed by a space.

