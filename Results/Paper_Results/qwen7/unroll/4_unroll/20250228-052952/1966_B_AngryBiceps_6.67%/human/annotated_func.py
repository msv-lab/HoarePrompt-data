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
        
        if len(set(a[0])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: The output state consists of multiple lines, each containing either 'YES' or 'NO'. For each test case, if the first row is uniform (all characters are the same) and different from the last row, or if any row is uniform and different from its corresponding first or last row, the output will be 'NO'. Otherwise, the output will be 'YES'. The number of lines equals the number of test cases provided as input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of size \(n \times m\) where \(1 \leq n, m \leq 500\), and each cell contains either 'W' or 'B'. For each test case, it checks if the first row is uniform and different from the last row, or if any row is uniform and different from its corresponding first or last row. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The function outputs one line per test case, totaling up to \(10^4\) lines.

