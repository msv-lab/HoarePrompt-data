#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, both positive integers such that 1 ≤ n, m ≤ 500, and a grid of size n × m where each cell contains either 'W' or 'B'. The sum of n·m over all test cases does not exceed 3·10^5.
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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' printed for each test case based on the conditions specified in the loop. For each test case, if the first row and the last row are identical and contain only one type of character ('W' or 'B'), or if every row is identical and contains only one type of character ('W' or 'B') but the first row is different from the last row, then 'NO' will be printed for that test case. Otherwise, 'YES' will be printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of size n x m where each cell contains either 'W' or 'B'. It reads the number of test cases, n and m for each test case, and the grid itself. For each test case, it checks if the first row and the last row are identical and contain only one type of character ('W' or 'B'), or if every row is identical and contains only one type of character but the first row is different from the last row. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value but prints the result for each test case.

