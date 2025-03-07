#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. Each test case starts with an integer n (2 ≤ n ≤ 10) representing the size of the grid. This is followed by n lines, each containing n characters which are either '0' or '1'. The grid in each test case contains exactly one triangle or exactly one square made up of '1's, and the size of the shape (k) is greater than 1.
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
        
    #State: The output state consists of `t` printed lines, each being either 'TRIANGLE', 'SQUARE', or an empty string, depending on the input strings for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an `n` by `n` grid of '0's and '1's. For each test case, it determines whether the grid contains exactly one triangle or exactly one square made up of '1's, with the size of the shape greater than 1. The function outputs 'TRIANGLE' if a triangle is detected and 'SQUARE' if a square is detected for each test case.

