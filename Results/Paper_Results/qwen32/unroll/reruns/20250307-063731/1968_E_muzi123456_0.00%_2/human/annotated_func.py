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
        
    #State: The variable `t` will be 0 after the loop finishes executing all its iterations. The variable `n` will hold the value of the last test case's input integer. The loop will have printed a sequence of numbers for each test case, where for each number `i` from 1 to `n`, it prints "1 i" on a new line, followed by a blank line after each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads another integer `n` and prints the numbers from 1 to `n`, each prefixed with "1", on separate lines. After processing each test case, it prints a blank line. The function does not return any value; its output is printed directly.

