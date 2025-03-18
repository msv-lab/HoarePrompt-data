#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 500. Each of the next n lines contains m characters, each of which is either 'W' or 'B'. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: For each test case, the program prints either 'YES' or 'NO' based on the conditions specified in the loop. The variable `t` (the number of test cases) is decremented to 0 after all test cases have been processed. The variables `n`, `m`, `a`, `first_row`, and `last_row` do not retain their values after each iteration as they are reinitialized in each loop iteration.
#Overall this is what the function does:The function processes multiple test cases where each test case consists of a grid of dimensions `n` by `m` filled with characters 'W' or 'B'. For each test case, it prints 'YES' if the grid does not meet the specific conditions where all elements in the first row are the same and different from the last row, or all elements in the first column are the same and different from the last column. Otherwise, it prints 'NO'.

