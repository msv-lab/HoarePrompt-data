#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 500. The grid is represented by a list of n strings, each of length m, consisting only of the characters 'W' and 'B'. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The output state consists of 'YES' or 'NO' printed for each test case based on the conditions specified in the loop. The variable `t` indicates the number of test cases processed, and for each test case, the grid properties are evaluated to determine if the output is 'YES' or 'NO'. The variables `n`, `m`, `a`, `first_row`, and `last_row` are reused for each test case without retaining their values from previous iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid defined by dimensions `n` and `m` and filled with characters 'W' and 'B'. For each test case, it evaluates the grid and prints 'NO' if either the first and last rows are identical and consist of the same character, or the first and last columns are identical and consist of the same character but are different from each other. Otherwise, it prints 'YES'.

