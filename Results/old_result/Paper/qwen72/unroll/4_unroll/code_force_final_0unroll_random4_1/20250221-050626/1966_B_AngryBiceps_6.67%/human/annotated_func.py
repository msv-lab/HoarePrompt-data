#State of the program right berfore the function call: The function `func` is expected to read input from stdin, where the first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with two integers n and m (1 ≤ n, m ≤ 500) representing the dimensions of the grid, followed by n lines each containing m characters 'W' or 'B' representing the initial colors of the grid. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop will have processed all test cases, and for each test case, it will have printed 'NO' if the first row of the grid is entirely one color ('W' or 'B') and different from the last row, or if the first column of the grid is entirely one color and different from the last column. Otherwise, it will have printed 'YES'. The variables `n`, `m`, `a`, `first_row`, and `last_row` will be reset for each test case, and their values will not persist between test cases.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case describes a grid of 'W' and 'B' characters. For each test case, it checks if the first row is entirely one color ('W' or 'B') and different from the last row, or if the first column is entirely one color and different from the last column. If either of these conditions is met, the function prints 'NO' for that test case; otherwise, it prints 'YES'. The function processes all test cases and prints the result for each one. The variables `n`, `m`, `a`, `first_row`, and `last_row` are reset for each test case, and their values do not persist between test cases.

