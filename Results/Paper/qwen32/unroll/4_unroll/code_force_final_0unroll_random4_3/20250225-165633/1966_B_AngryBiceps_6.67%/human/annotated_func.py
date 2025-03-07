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
        
        if len(set(a[0])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: t is 0, and the variables n, m, a, first_row, and last_row do not hold any specific values as they are reassigned in each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a grid of dimensions `n` by `m` filled with characters 'W' or 'B'. For each test case, it determines whether the grid meets a specific condition: it prints 'NO' if the first row is uniform (all characters are the same) and different from the last row, or if the first column (formed by the first character of each row) is uniform and different from the last column (formed by the last character of each row). Otherwise, it prints 'YES'.

