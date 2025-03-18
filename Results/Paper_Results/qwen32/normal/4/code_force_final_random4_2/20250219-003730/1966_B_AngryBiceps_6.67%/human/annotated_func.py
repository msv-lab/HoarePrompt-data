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
        
    #State: The loop has processed all `t` test cases. For each test case, it has determined whether the given grid of 'W' and 'B' characters meets the specified conditions and printed either 'YES' or 'NO'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of 'W' and 'B' characters. For each grid, it checks if all characters in the first row are the same and different from the last row, or if all characters in the first column are the same and different from the last column. If either condition is met, it outputs 'NO'; otherwise, it outputs 'YES'.

