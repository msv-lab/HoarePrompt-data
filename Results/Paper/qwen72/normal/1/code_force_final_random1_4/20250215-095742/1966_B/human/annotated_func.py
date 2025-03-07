#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of two integers n and m (1 ≤ n, m ≤ 500), representing the dimensions of the grid, followed by n lines, each containing m characters 'W' or 'B', representing the colors of the grid cells. The total number of cells across all test cases does not exceed 3 × 10^5.
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
        
    #State: After all iterations, `t` is the original value provided by the user, `tc` is `t - 1`, `n` and `m` are the dimensions of the grid for the last test case, `gr` is a list containing `n` strings representing the grid for the last test case, `i` is `n - 1`, `j` is `m - 2`, and `ans` is either 'YES' or 'NO' based on the conditions checked in the loop for each test case. For each test case, if the top-left cell (`gr[0][0]`) is different from the bottom-right cell (`gr[n-1][m-1]`), and all cells in the first row and last row are the same, and all cells in the first column and last column are the same, then `ans` is 'NO'. Otherwise, `ans` is 'YES'.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case involves a grid of dimensions n x m with cells colored 'W' or 'B'. For each test case, the function checks if the top-left cell is different from the bottom-right cell. If they are different and all cells in the first and last rows are the same, and all cells in the first and last columns are the same, the function outputs 'NO'. Otherwise, it outputs 'YES'. The function prints the result for each test case and does not return any value. After processing all test cases, the function concludes without modifying any global state.

