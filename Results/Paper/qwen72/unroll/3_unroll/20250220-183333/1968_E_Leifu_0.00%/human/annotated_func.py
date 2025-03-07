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
        
    #State: The loop has finished executing for all `t` test cases. For each test case, the values of `n` have been processed as specified in the loop, printing the pairs as described. The value of `t` remains unchanged, and the final value of `n` is the last input integer provided for the `t`-th test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 50`, representing the number of test cases. For each test case, it reads an integer `n` from the input, where `2 <= n <= 10^3`. The function then prints specific pairs of integers for each test case. Specifically, it prints the pairs `(1, 1)` and `(1, 2)`. If `n` is 3, it prints the pair `(2, 3)`. Otherwise, it prints the pairs `(2, 4)` and then for each integer `j` from 4 to `n` (inclusive), it prints the pair `(j, j)`. After processing all test cases, the function has no return value, and the final state of the program is that `t` remains unchanged, and the last value of `n` is the input provided for the `t`-th test case.

