#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, both positive integers such that 1 ≤ n, m ≤ 500, and a grid of size n × m where each cell contains either 'W' or 'B'. The sum of n·m over all test cases does not exceed 3·10^5.
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
        
    #State: The final value of `tc` is `t-1`, `t` remains the same, `n` and `m` remain as their last values entered during the loop's execution, `gr` is a list containing exactly `n` elements, each being a string representing a row of the grid as input during the loop's execution, `i` is `n-1` (the last index of the list `gr`), `ans` is either 'NO' or 'YES' based on the final evaluation of the conditions inside the loop.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of a grid of up to 500x500 cells, where each cell contains either 'W' or 'B'. For each test case, it checks if the top-left cell is the same as the bottom-right cell. If they are different, it checks if all cells in the first row and first column are the same, and if all cells in the last row and last column are the same. Based on these checks, it determines whether the grid meets certain conditions and prints either 'YES' or 'NO' for each test case.

