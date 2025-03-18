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
        
    #State: The variable `t` remains unchanged, and for each of the `t` test cases, the variable `n` is processed and printed according to the loop logic. The loop prints '1 1', '1 2', '2 3' if `n` is 3, or '2 4' followed by pairs of integers from '4 4' to 'n n' if `n` is greater than 3.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer between 1 and 50, inclusive. For each test case, it reads an integer `n` between 2 and 10^3, inclusive, and prints specific pairs of integers. It always prints '1 1' and '1 2'. If `n` is 3, it prints '2 3'. If `n` is greater than 3, it prints '2 4' followed by pairs of integers from '4 4' to 'n n'. The function does not return any value. After the function concludes, the variable `t` remains unchanged, and each `n` for the test cases has been processed and printed according to the specified logic.

