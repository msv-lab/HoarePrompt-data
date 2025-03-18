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
        
    #State: `t` is an input integer such that 1 <= t <= 50, `i` is `t - 1`. For each of the `t` test cases, if `n` is 3, the value of `n` remains 3. If `n` is greater than or equal to 4, `j` is set to `n + 1`.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer between 1 and 50. For each test case, it reads an integer `n` between 2 and 10^3. It then prints the pairs (1, 1) and (1, 2). If `n` is 3, it prints the pair (2, 3). If `n` is greater than 3, it prints the pair (2, 4) and then prints pairs (j, j) for all integers `j` from 4 to `n`. After processing all test cases, the function concludes without returning any value.

