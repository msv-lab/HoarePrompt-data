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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' responses based on the conditions checked within the loop for each test case. For each test case, if the first row and the last row are identical and contain only one type of character ('W' or 'B'), or if the entire first and last rows of the grid are uniform but different from each other, the output will be 'NO'. Otherwise, the output will be 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of size n × m where each cell contains either 'W' or 'B'. For each test case, it checks if the first and last rows are identical and contain only one type of character ('W' or 'B'), or if the entire first and last rows of the grid are uniform but different from each other. If either condition is met, it outputs 'NO'; otherwise, it outputs 'YES'. The function does not return any value but prints the result for each test case.

