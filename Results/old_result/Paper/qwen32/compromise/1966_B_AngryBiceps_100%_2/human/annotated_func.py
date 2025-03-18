#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 500. The grid is represented by n lines, each containing m characters, where each character is either 'W' (white) or 'B' (black). The sum of n*m over all test cases does not exceed 3*10^5.
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
        
    #State: The loop will have processed all `t` test cases, each determining if a grid of `n` by `m` size, with characters 'W' or 'B', meets the specified conditions. For each test case, the program checks if the first and last rows of the grid are composed of the same character and are different from each other, or if the first and last columns of the grid are composed of the same character and are different from each other. If either of these conditions is met, it prints 'NO'; otherwise, it prints 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of 'W' and 'B' characters. For each grid, it checks if the first and last rows are composed of the same character and are different from each other, or if the first and last columns are composed of the same character and are different from each other. If either condition is met, it outputs 'NO'; otherwise, it outputs 'YES'.

