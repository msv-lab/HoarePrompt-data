#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each test case consists of two integers n and m such that 1 <= n, m <= 500, followed by n lines of m characters each, where each character is either 'W' or 'B'. The sum of n * m over all test cases does not exceed 3 * 10^5.
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
        
    #State: 
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of 'W' and 'B' characters. For each grid, it determines if it's possible to change all characters to the same color ('W' or 'B') by only changing characters in the first row or the last row, or the first column or the last column, while maintaining the condition that no two adjacent characters in the first or last row, or the first or last column, differ. It prints 'YES' if it's possible, otherwise 'NO'.

