#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, both positive integers such that 1 ≤ n, m ≤ 500, and a grid of size n × m filled with characters 'W' and 'B'. The sum of n·m over all test cases does not exceed 3·10^5.
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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' printed based on the conditions evaluated within the loop for each test case. For each test case, if the first row and last row are identical and filled with the same character, or if the entire grid's first and last rows meet specific conditions where they are different but their characters are uniform across the respective rows, it will print 'NO'. Otherwise, it will print 'YES'. This process repeats for each test case provided by the input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of size n x m where n and m are positive integers up to 500, and each cell contains either 'W' or 'B'. It reads the number of test cases, followed by the dimensions and content of each grid. For each grid, it checks if the first and last rows are identical and filled with the same character, or if the first and last rows are different but have uniform characters across them. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The function outputs a series of 'YES' and 'NO' based on these conditions for each test case.

