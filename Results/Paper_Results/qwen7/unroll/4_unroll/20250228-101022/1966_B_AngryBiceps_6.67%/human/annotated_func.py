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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' printed based on the conditions checked within the loop for each test case. For each test case, if the first row is uniform and different from the last row, or if any row is uniform and different from its corresponding column's start and end characters, it prints 'NO', otherwise it prints 'YES'. The number of 'YES' and 'NO' will depend on the input provided for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of size n x m where n and m are positive integers up to 500. For each test case, it reads the grid and checks if the first row is uniform and different from the last row, or if any row is uniform and different from its corresponding column's start and end characters. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The function outputs a series of 'YES' and 'NO' based on these conditions for each test case.

