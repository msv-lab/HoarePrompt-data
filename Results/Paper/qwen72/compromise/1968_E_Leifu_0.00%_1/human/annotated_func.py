#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^3.
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
        
    #State: `n` is an input integer, `t` must be greater than or equal to the initial value of `t`, and `i` is `t - 1`. If `n` is 3, there are no changes to the variables. If `n` is greater than or equal to 4, `j` is set to `n`. If `n` is less than 3, `j` is set to `n`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, and for each of the `t` test cases, it reads another integer `n` where 2 <= n <= 10^3. For each test case, it prints the pairs (1, 1), (1, 2), and if `n` is 3, it prints (2, 3). If `n` is greater than 3, it prints (2, 4) followed by pairs (j, j) for all integers `j` from 4 to `n` inclusive. The function does not return any value. After the function concludes, the program state is such that `t` test cases have been processed, and the corresponding output has been printed for each `n` input.

