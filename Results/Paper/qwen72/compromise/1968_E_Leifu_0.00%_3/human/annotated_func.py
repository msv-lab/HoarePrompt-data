#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and n is an integer for each test case such that 2 <= n <= 10^3.
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
        
    #State: `t` is an input integer such that 1 <= t <= 50, `i` is `t - 1`. If `n` == 3, there are no changes to `t`, `i`, or `n`. Otherwise, `n` must be greater than or equal to 4, and `j` is set to `n` for the last iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 50`. It then processes `t` test cases, each involving an integer `n` such that `2 <= n <= 10^3`. For each test case, the function prints the pairs `(1, 1)`, `(1, 2)`, and either `(2, 3)` if `n == 3` or `(2, 4)` followed by pairs `(j, j)` for `j` ranging from 4 to `n` if `n >= 4`. After processing all test cases, the function does not return any value, and the final state of the program is that `t` test cases have been processed and the corresponding pairs have been printed.

