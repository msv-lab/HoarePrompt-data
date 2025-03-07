#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the first line contains two integers n and m (1 ≤ n, m ≤ 500) representing the dimensions of the grid. The next n lines contain m characters each, which are either 'W' or 'B', representing the initial colors of the squares in the grid. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: All test cases have been processed, and for each test case, the program has printed either 'YES' or 'NO' based on the conditions specified in the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of dimensions `n` by `m` filled with 'W' or 'B'. For each test case, it prints 'YES' if the grid meets certain conditions (either the first row is not uniform or the first and last rows are the same), otherwise it prints 'NO'.

