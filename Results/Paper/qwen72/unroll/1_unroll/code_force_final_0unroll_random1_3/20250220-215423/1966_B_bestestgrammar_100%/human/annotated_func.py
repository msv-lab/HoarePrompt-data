#State of the program right berfore the function call: The function `func` is expected to read input from standard input, where the first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with two integers n and m (1 ≤ n, m ≤ 500) representing the dimensions of the grid, followed by n lines, each containing m characters 'W' or 'B' representing the initial colors of the grid. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop has finished executing all iterations. The variable `t` is now 0, as the loop has run `t` times. The variables `n`, `m`, `gr`, and `ans` are no longer in scope, as they are defined within the loop and are reset for each test case. The output for each test case is printed as 'YES' or 'NO' based on the conditions checked within the loop.
#Overall this is what the function does:The function `func` reads input from standard input, where the first line contains an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m` representing the dimensions of a grid, followed by `n` lines each containing `m` characters ('W' or 'B') representing the initial colors of the grid. The function then checks if it is possible to transform the grid so that the top-left and bottom-right corners have the same color by only changing the colors of the cells on the borders. If it is possible, the function prints 'YES' for that test case; otherwise, it prints 'NO'. After processing all test cases, the function concludes, and the output for each test case is printed.

