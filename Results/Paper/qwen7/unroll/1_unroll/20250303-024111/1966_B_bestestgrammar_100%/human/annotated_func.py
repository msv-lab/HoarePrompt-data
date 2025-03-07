#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, both positive integers such that 1 ≤ n, m ≤ 500, and the grid is represented by n lines, each containing m characters 'W' (white) and 'B' (black), with the guarantee that the total number of characters (n * m) across all test cases does not exceed 3 * 10^5.
def func():
    t = int(input())
    for tc in range(t):
        n, m = map(int, input().split())
        
        gr = []
        
        for i in range(n):
            gr.append(input())
        
        ans = 'YES'
        
        if gr[0][0] != gr[n - 1][m - 1]:
            impossible = True
            for j in range(m - 1):
                if gr[0][j] != gr[0][j + 1] or gr[n - 1][j] != gr[n - 1][j + 1]:
                    impossible = False
            if impossible:
                ans = 'NO'
            impossible = True
            for i in range(n - 1):
                if gr[i][0] != gr[i + 1][0] or gr[i][m - 1] != gr[i + 1][m - 1]:
                    impossible = False
            if impossible:
                ans = 'NO'
        
        print(ans)
        
    #State: Output State: t is an input integer, within the range 1 ≤ t ≤ 10^4. After executing all iterations of the loop, the variable ans is set to 'YES' unless there is a condition where the first element of the first row does not match the last element of the last row, and it's impossible to make all corresponding elements equal by swapping columns or rows.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid represented by `n` rows and `m` columns containing 'W' (white) and 'B' (black) characters. For each test case, it checks if it's possible to make the top-left element of the grid equal to the bottom-right element by swapping any number of rows or columns. If such swaps can make the elements equal, the function outputs 'YES'; otherwise, it outputs 'NO'. The function reads the number of test cases `t`, followed by the dimensions `n` and `m` and the grid configuration for each test case, and prints the result for each test case.

