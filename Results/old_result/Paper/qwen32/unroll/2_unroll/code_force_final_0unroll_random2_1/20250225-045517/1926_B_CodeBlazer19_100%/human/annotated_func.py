#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, the input contains an integer n (2 ≤ n ≤ 10) representing the size of the grid, followed by n lines each containing n characters that are either '0' or '1'. It is guaranteed that the grid contains exactly one triangle or exactly one square composed of '1's, and the size of the shape (k) is greater than 1.
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
        
    #State: a series of 'TRIANGLE' or 'SQUARE' printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of '0's and '1's. For each grid, it determines whether the grid contains a shape composed entirely of '1's that forms a triangle or a square, and then prints the type of shape ("TRIANGLE" or "SQUARE") for each test case.

