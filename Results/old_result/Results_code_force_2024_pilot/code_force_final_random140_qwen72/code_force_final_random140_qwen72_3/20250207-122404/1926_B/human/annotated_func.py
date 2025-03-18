#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 10, representing the size of the grid. Each grid is represented by n lines, each containing n characters ('0' or '1'). The grid contains exactly one triangle or one square that includes all '1's, and the shape cannot consist of exactly one '1'.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = 0
        
        b = ''
        
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'Triangle'
            elif s.count('1') > 1:
                b = 'Square'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: `t` is 0, `i` is `t-1`, `n` is the last input integer, `j` is `n-1`, and `s` is the last input string processed. If any of the input strings contained exactly one '1' character, `a` is 'Triangle'. Otherwise, `a` is 0. If any of the input strings contained more than one '1' character, `b` is 'Square'. Otherwise, `b` is an empty string.
#Overall this is what the function does:The function reads a series of test cases, each consisting of an integer `n` and an `n x n` grid represented by `n` lines of `n` characters ('0' or '1'). For each test case, it determines and prints whether the grid contains a 'Triangle' (if any row has exactly one '1') or a 'Square' (if any row has more than one '1'). If no row has exactly one '1', the function will always print 'Square'. The function does not return any value; it only prints the result for each test case. After processing all test cases, the function concludes.

