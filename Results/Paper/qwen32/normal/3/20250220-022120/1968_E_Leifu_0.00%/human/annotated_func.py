#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: The loop has executed `t` times, where `t` is the number of test cases. For each test case, the program prints '1 1', '1 2', and then either '2 3' if `n` is 3, or '2 4' followed by each integer from 4 to `n` printed twice on its respective line if `n` is greater than 3.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints a series of pairs of integers according to specific rules. It prints '1 1', '1 2', and then either '2 3' if `n` is 3, or '2 4' followed by each integer from 4 to `n` printed twice on its respective line if `n` is greater than 3.

