#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, both positive integers such that 1 ≤ n, m ≤ 500, and a grid of size n × m where each cell contains either 'W' or 'B'. The sum of n × m over all test cases does not exceed 3 × 10^5.
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
        
    #State: All test cases have been processed, and the final state of the variables is as follows: `a` is a list containing `n` elements for each test case, where `n` is the number of rows in the grid for that test case. Each element in `a` is a string representing a row of the grid. `first_row` is a string consisting of the first character of each row in `a`. `last_row` is a string consisting of the last character of each row in `a`. The variable `i` is `-1`, indicating that the loop has completed all its iterations for all test cases. For each test case, if the conditions specified in the loop body are met (either the first and last rows are uniform but different, or neither the first nor the last row is uniform), the output is 'NO'. Otherwise, the output is 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of size n x m where n and m are positive integers up to 500, and each cell contains either 'W' or 'B'. For each test case, it checks if the first and last rows of the grid are uniform (all characters the same) but different from each other, or if the first and last characters of each row are uniform but different from each other. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function outputs the results for each case.

