#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 500. The grid is represented by n lines, each containing m characters which are either 'W' or 'B'. The sum of n*m over all test cases does not exceed 3*10^5.
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
        
        if len(set(a[0])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: The output state consists of a series of 'YES' or 'NO' responses, each corresponding to a test case. For each test case, the response is 'NO' if either the first row is uniform (all 'W' or all 'B') and different from the last row, or if the first column is uniform and different from the last column. Otherwise, the response is 'YES'. The values of t, n, m, a, first_row, and last_row are not preserved between test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of 'W' and 'B' characters. For each grid, it determines if the first row is uniform and different from the last row, or if the first column is uniform and different from the last column. If either condition is true, it outputs 'NO'; otherwise, it outputs 'YES'.

