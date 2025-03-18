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
        
    #State: `t` is an integer such that 1 <= `t` <= 50, `i` is `t-1` (indicating the loop has completed all `t` iterations), `n` is the integer input by the user for the last test case. If `n` is 3 for the last test case, `j` is either undefined or retains its previous value from the last iteration where it was defined. If `n` is greater than or equal to 4 for the last test case, `j` is equal to `n`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads an integer `n` such that 2 <= n <= 10^3. It then prints a series of pairs of integers based on the value of `n`. Specifically, it prints '1 1', '1 2', and either '2 3' if `n` is 3, or '2 4' followed by pairs 'j j' for each `j` from 4 to `n` if `n` is greater than 3.

