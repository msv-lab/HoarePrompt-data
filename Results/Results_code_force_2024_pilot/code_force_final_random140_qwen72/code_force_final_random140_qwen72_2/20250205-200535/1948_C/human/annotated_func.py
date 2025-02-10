#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an even integer such that 2 ≤ n ≤ 2·10^5, representing the number of columns in the grid. The grid consists of 2 rows, and each cell contains an arrow represented by a character '<' or '>', indicating the direction of the arrow. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for j in range(int(input())):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('NO')
                break
        else:
            print('YES')
        
    #State: `j` is `t - 1`, `n` is an input integer greater than 0, `a` is an input string, `b` is an input string. The loop has completed all iterations without breaking. The final value of `i` is the largest odd number less than `n`. If the loop did not break, the program prints 'YES'.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads the number of test cases `t` (1 ≤ t ≤ 10^4) and for each test case, it reads an even integer `n` (2 ≤ n ≤ 2·10^5) representing the number of columns in a 2-row grid. Each cell in the grid contains an arrow ('<' or '>'). The function checks if there exists any pair of adjacent cells in the same row or in the opposite row where both arrows point left ('<'). If such a pair is found, the function prints 'NO' for that test case; otherwise, it prints 'YES'. After processing all test cases, the function completes its execution.

