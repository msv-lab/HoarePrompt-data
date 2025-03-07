#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 500. The grid is represented by a list of n strings, each of length m, containing only the characters 'W' and 'B'. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: A series of 'YES' or 'NO' answers, one for each test case, based on the conditions specified in the code.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a grid of dimensions `n` by `m` filled with the characters 'W' and 'B'. For each test case, it determines if the grid can be considered valid based on specific conditions: if the top-left and bottom-right corners are different, then every cell in the first and last rows must be the same, and every cell in the first and last columns must be the same. It outputs 'YES' if the grid meets these conditions for each test case, otherwise 'NO'.

