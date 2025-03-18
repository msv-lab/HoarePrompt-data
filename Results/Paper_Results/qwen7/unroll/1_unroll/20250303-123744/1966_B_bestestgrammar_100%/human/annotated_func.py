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
        
    #State: Output State: t is an input integer; for each tc in range(t), n and m are integers read from input, gr is a list of n strings read from input, ans is initially set to 'YES', and after processing the grid, ans is printed as either 'YES' or 'NO' based on certain conditions.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of size \(n \times m\) where \(n\) and \(m\) are positive integers between 1 and 500, and each cell in the grid contains either 'W' or 'B'. For each test case, the function determines whether it is possible to traverse from the top-left corner to the bottom-right corner of the grid such that every step moves only to adjacent cells and maintains the same color. If such a traversal is possible, the function prints 'YES'; otherwise, it prints 'NO'.

