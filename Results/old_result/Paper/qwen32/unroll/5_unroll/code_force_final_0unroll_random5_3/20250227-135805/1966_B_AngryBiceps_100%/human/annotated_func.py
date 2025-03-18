#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the following t test cases consists of an integer n and an integer m where 1 ≤ n, m ≤ 500, followed by n lines each containing m characters which are either 'W' or 'B'. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The output state consists of t lines, each containing either 'YES' or 'NO', based on the conditions specified in the loop for each test case. The variable t remains unchanged, and for each of the t test cases, the variables n, m, a, first_row, and last_row are recalculated and used to determine the output for that test case without affecting the state of t or any other variables outside the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of dimensions `n` by `m` filled with characters 'W' or 'B'. For each test case, it determines whether the grid meets specific conditions: if the first and last rows are identical and consist of the same character, or if the first and last columns are identical and consist of the same character. If either condition is true, it outputs 'NO'; otherwise, it outputs 'YES'.

