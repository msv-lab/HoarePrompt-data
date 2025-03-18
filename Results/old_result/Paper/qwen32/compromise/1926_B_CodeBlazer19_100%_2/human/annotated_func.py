#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 2 <= n <= 10, and the grid is an n x n list of strings where each string consists of n characters, each character being either '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid, and the size of the triangle or square is greater than 1.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = 0
        
        b = ''
        
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'TRIANGLE'
            elif s.count('1') > 1:
                b = 'SQUARE'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: `t` is an input integer between 1 and 100, inclusive; `i` is `t`; `n` is the input integer between 2 and 10 from the last iteration; the grid is an `n x n` list of strings where each string consists of `n` characters, each character being either '0' or '1', and the grid contains exactly one triangle or exactly one square that contains all the '1's in the grid, and the size of the triangle or square is greater than 1; `a` is 'TRIANGLE' if the last grid contains exactly one triangle, otherwise `a` is 0; `b` is 'SQUARE' if the last grid contains exactly one square, otherwise `b` is ''; `j` is `n-1`; `s` is the last input string from the last grid.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and an `n x n` grid of strings consisting of '0's and '1's. It then determines whether the '1's in the grid form exactly one triangle or exactly one square, with the size of the shape being greater than 1, and prints the type of shape ('TRIANGLE' or 'SQUARE') for each test case.

