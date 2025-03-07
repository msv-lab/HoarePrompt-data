#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. Each test case consists of two integers n and m (1 ≤ n, m ≤ 500), representing the dimensions of the grid, followed by n lines each containing m characters ('W' or 'B'), representing the initial colors of the grid. The total number of cells across all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is an input integer between 1 and 10^4, `tc` is `t - 1`, `n` is an input integer, `m` is an input integer, `gr` is a list containing `n` input strings, `i` is `n - 1`, `ans` is either 'YES' or 'NO'. For each test case, if `gr[0][0]` is different from `gr[n - 1][m - 1]` and all rows and columns have consistent colors except possibly the corners, `ans` is 'NO'. Otherwise, `ans` is 'YES'.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by a grid of dimensions `n` x `m` filled with characters 'W' or 'B'. For each test case, it checks if the top-left corner cell (`gr[0][0]`) and the bottom-right corner cell (`gr[n-1][m-1]`) are the same color. If they are different, it further checks if all rows and columns have consistent colors except possibly the corners. If these conditions are met, the function prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function completes without returning any value.

