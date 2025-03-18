#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there are two integers n and m (1 ≤ n, m ≤ 500) representing the dimensions of the grid. Following these integers, there are n lines, each containing a string of m characters ('W' or 'B') representing the initial colors of the squares in the grid. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The variable `t` remains unchanged as it represents the number of test cases. For each test case, the output is either 'YES' or 'NO' based on the conditions checked within the loop. The grid `gr` and the variables `n`, `m`, and `ans` are specific to each iteration and do not persist after the loop completes. The final output consists of `t` lines, each containing 'YES' or 'NO' corresponding to the result of each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of dimensions `n` by `m` filled with 'W' or 'B'. For each grid, it determines if it is possible to paint the grid such that all cells in the first row are the same color, all cells in the last row are the same color, all cells in the first column are the same color, and all cells in the last column are the same color, with the additional condition that the top-left and bottom-right cells must be the same color if the grid is to be painted in this manner. The function outputs 'YES' if such a painting is possible for each test case, otherwise it outputs 'NO'.

