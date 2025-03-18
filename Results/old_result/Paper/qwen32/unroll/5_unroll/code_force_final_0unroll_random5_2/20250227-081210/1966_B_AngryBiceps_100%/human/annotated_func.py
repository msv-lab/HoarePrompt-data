#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 500. The grid is represented by n lines, each containing m characters that are either 'W' or 'B'. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The output state consists of 'YES' or 'NO' printed for each test case based on the conditions specified in the loop. The variable `t` remains unchanged and represents the number of test cases. For each test case, the grid is defined by `n` rows and `m` columns, with each cell containing either 'W' or 'B'. The variable `a` stores the grid as a list of strings, where each string represents a row. The strings `first_row` and `last_row` are constructed by concatenating the first and last characters of each row, respectively. The output for each test case is determined by whether all characters in the first and last rows (or columns) are the same and different from each other. If either condition is met, the output is 'NO'; otherwise, it is 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of 'W' and 'B' characters. For each test case, it determines if the first and last rows or the first and last columns of the grid are uniform (all the same character) and different from each other. If either condition is true, it outputs 'NO'; otherwise, it outputs 'YES'.

