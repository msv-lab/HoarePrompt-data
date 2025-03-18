#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 500. The grid is represented by n lines, each containing m characters, where each character is either 'W' or 'B'. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\); `n` and `m` are integers such that 1 ≤ `n`, `m` ≤ 500; `tc` ranges from 0 to `t-1`; `gr` is a list containing `n` strings read from the input for each test case; `ans` is 'YES' or 'NO' based on the conditions specified in the code; all test cases have been processed.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a grid of dimensions `n` by `m` filled with 'W' and 'B'. It checks if the grid can be considered "valid" based on specific conditions related to the corners and edges of the grid. For each test case, it prints 'YES' if the grid meets the criteria or 'NO' otherwise.

