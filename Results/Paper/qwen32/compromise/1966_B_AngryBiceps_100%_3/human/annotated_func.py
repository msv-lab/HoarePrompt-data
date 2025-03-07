#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 500. The grid is represented by n lines, each containing m characters, where each character is either 'W' or 'B'. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop has processed all `t` test cases. For each test case, it has determined whether the conditions for printing 'NO' are met and printed 'NO' if they are; otherwise, it has printed 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of dimensions `n` by `m` filled with characters 'W' or 'B'. For each grid, it determines whether the grid meets specific conditions that would result in printing 'NO'; otherwise, it prints 'YES'. The conditions for printing 'NO' are that either the first and last rows are uniform in color but different from each other, or the first and last columns are uniform in color but different from each other.

