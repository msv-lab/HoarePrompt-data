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
        
    #State: The loop has processed all `t` test cases. For each test case, it has read the integers `n` and `m`, then read `n` lines of `m` characters each into the list `a`. It has constructed `first_row` and `last_row` by concatenating the first and last characters of each row in `a`, respectively. For each test case, it has printed 'NO' if the first row consists of identical characters and is not equal to the last row, or if the first column consists of identical characters and is not equal to the last column. Otherwise, it has printed 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of dimensions `n` by `m` filled with characters 'W' or 'B'. For each test case, it determines if the grid meets a specific condition: it prints 'NO' if the first row is uniform (all characters are the same) and different from the last row, or if the first column is uniform and different from the last column. Otherwise, it prints 'YES'.

