#State of the program right berfore the function call: The function should take two integers n and m, and a list of n strings, each of length m, containing characters 'W' and 'B' representing the colors of the grid. n and m are such that 1 ≤ n, m ≤ 500, and the total number of elements in all test cases does not exceed 3·10^5.
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
        
    #State: The loop will execute `t` times, and for each iteration, it will read `n` and `m` from input, followed by `n` lines of strings each of length `m`. After processing, it will print 'YES' or 'NO' based on the conditions described in the loop. The variables `gr`, `ans`, and `impossible` will be reset for each iteration. After all iterations, the loop will have printed `t` lines, each containing either 'YES' or 'NO'. The values of `t`, `n`, and `m` will remain unchanged, and the list `gr` will be empty.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `m`, and a list of `n` strings, each of length `m`, containing characters 'W' and 'B'. It then checks if the grid can be transformed into a valid configuration where the top-left and bottom-right corners have the same color, and if the entire first row, last row, first column, and last column are uniform in color. If the grid meets these conditions, it prints 'YES'; otherwise, it prints 'NO'. The function performs this check for each of the `t` test cases and prints the result for each case. After all iterations, the loop will have printed `t` lines, each containing either 'YES' or 'NO'. The values of `t`, `n`, and `m` remain unchanged, and the list `gr` is reset to empty for each iteration.

