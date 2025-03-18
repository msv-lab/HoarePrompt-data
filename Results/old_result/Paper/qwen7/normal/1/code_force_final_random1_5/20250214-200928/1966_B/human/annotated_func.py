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
        
    #State: tc is equal to the total number of test cases (t), n and m are integers representing dimensions of the grid, gr is a list of strings representing the grid, ans is 'NO', impossible is True, and both j and i are set to their maximum possible values within the loop (j is m - 2 and i is n - 1).
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of size n x m where each cell contains either 'W' or 'B'. For each test case, it checks if the top-left cell is the same as the bottom-right cell. If they differ, it further checks if the first row or the last column can be uniform without changing the top-left and bottom-right cells. Based on these checks, it determines whether it's possible to make the top-left and bottom-right cells the same by flipping rows or columns, and prints 'YES' if possible, otherwise 'NO'.

