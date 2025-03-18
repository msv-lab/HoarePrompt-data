#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n and m are integers such that 1 <= n, m <= 500, and the grid is a list of n strings, each of length m, containing only the characters 'W' and 'B'.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = []
        
        first_row = ''
        
        last_row = ''
        
        for i in range(n):
            a.append(input())
            first_row += a[-1][0]
            last_row += a[-1][-1]
        
        if len(set(a[0])) == 1 and len(set(a[-1])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and len(set(last_row)
            ) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: The loop executes for `t` iterations, and for each iteration, it reads `n` and `m` from input, constructs a grid `a` of size `n` by `m` from input, and checks if the first row and last row of the grid are either entirely 'W' or 'B' and different from each other, or if the first and last columns of the grid are entirely 'W' or 'B' and different from each other. If either condition is true, it prints 'NO'. Otherwise, it prints 'YES'. After all iterations, the variables `t`, `n`, `m`, and the grid `a` are no longer in scope, and the initial state variables `t`, `n`, and `m` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from input, indicating the number of test cases. For each test case, it reads two integers `n` and `m` from input, representing the dimensions of a grid, and then reads `n` strings of length `m` to construct the grid. The function checks if the first row and last row of the grid are entirely composed of the same character ('W' or 'B') and are different from each other, or if the first column and last column of the grid are entirely composed of the same character and are different from each other. If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. After processing all `t` test cases, the function concludes, and the variables `t`, `n`, `m`, and the grid `a` are no longer in scope.

