#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with two integers n and m (1 ≤ n, m ≤ 500) representing the dimensions of the grid. This is followed by n lines, each containing m characters 'W' or 'B' representing the colors of the squares in the grid. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: For each test case, the variable `ans` will be either 'YES' or 'NO' based on the conditions specified in the loop. The variable `ans` is 'YES' if the top-left and bottom-right corners of the grid are the same color, or if there is at least one adjacent pair of cells in the top row or the bottom row that have different colors, or at least one adjacent pair of cells in the first and last columns that have different colors. The variable `ans` is 'NO' if the top-left and bottom-right corners of the grid are different colors and all cells in the top row and bottom row are the same color, and all cells in the first and last columns are the same color. The variables `t`, `n`, `m`, and `gr` will be in their final states after processing all test cases, where `t` will be 0 (as all test cases have been processed), `n` and `m` will be the dimensions of the last test case, and `gr` will be the grid of the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of 'W' and 'B' characters. For each grid, it determines if it's possible to change the color of some cells such that the top-left and bottom-right corners have the same color, either directly or by ensuring that there is at least one pair of adjacent cells in the top or bottom row with different colors, or at least one pair of adjacent cells in the first or last column with different colors. The function outputs 'YES' if such a configuration is possible and 'NO' otherwise.

