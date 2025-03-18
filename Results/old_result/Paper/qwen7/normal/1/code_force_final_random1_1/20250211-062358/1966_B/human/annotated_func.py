#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and m, both positive integers such that 1 ≤ n, m ≤ 500, and a grid of size n × m filled with characters 'W' and 'B' representing white and black squares respectively. The sum of n·m over all test cases does not exceed 3·10^5.
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
        
    #State: `tc` is 3, `i` is `n - 2`, `ans` is 'NO', `impossible` is True, `n` is greater than 1, `m` is greater than 3, `gr` is a list containing `n` elements where the first element is not equal to the last element.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of a grid of size n x m (where 1 ≤ n, m ≤ 500) filled with 'W' and 'B'. For each test case, it checks if the top-left and bottom-right cells of the grid are the same color. If they are different, it further checks if all cells in the first row and last column are the same color. Based on these checks, it determines whether the grid meets certain conditions and prints 'YES' if it does, otherwise 'NO'.

