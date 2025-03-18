#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 500. The grid is represented by n lines, each containing m characters which are either 'W' or 'B'. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The variable `t` iterations have completed, and for each iteration, the program has read `n` and `m`, then read `n` lines of input each containing `m` characters ('W' or 'B'). It has checked if the first and last rows are identical or if the first and last columns are identical and not the same. If either condition is met, it printed 'NO'; otherwise, it printed 'YES'. The state of `t`, `n`, `m`, `a`, `first_row`, and `last_row` from the last iteration remains, but no further iterations are executed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the dimensions of a grid (n x m) and the grid itself, which consists of 'W' and 'B' characters. It then determines if the first and last rows of the grid are identical or if the first and last columns are identical and not the same. If either condition is true, it outputs 'NO'; otherwise, it outputs 'YES'.

