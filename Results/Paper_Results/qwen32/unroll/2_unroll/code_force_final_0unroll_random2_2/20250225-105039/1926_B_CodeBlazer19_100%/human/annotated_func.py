#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 2 <= n <= 10, and the grid is an n x n list of lists containing only the characters '0' and '1'. Each grid contains exactly one triangle or exactly one square that consists of all the '1's. The size of the triangle or square is greater than 1 (i.e., it consists of more than one '1').
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
        
    #State: t test cases each resulting in the output 'SQUARE'.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an `n x n` grid of '0's and '1's. For each grid, it determines whether the shape formed by the '1's is a triangle or a square, with the shape size being greater than 1, and prints the type of shape.

