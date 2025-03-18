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
        
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each tc in range(t), n and m are positive integers, gr is a list of n strings, each string has length m. After processing the grid according to the given logic, ans is either 'YES' or 'NO'.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a grid of size n x m where n and m are positive integers (1 ≤ n, m ≤ 500) and each cell contains either 'W' or 'B'. For each test case, the function checks if the top-left cell is the same as the bottom-right cell. If they are different, it checks if all cells in the first row and first column are the same, and if all cells in the last row and last column are the same. Based on these checks, the function sets the variable `ans` to either 'YES' or 'NO', indicating whether the conditions are met. Finally, the function prints `ans` for each test case.

