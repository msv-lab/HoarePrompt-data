#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the input consists of t test cases, each test case starts with an integer n followed by n lines, each containing n characters that are either '0' or '1', and the grid contains exactly one triangle or exactly one square that contains all the '1's in the grid, with the size of the triangle or square being greater than 1.
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
        
    #State: t is an integer between 1 and 100, i is 99, a is 'TRIANGLE' if any of the strings s entered during the loop iterations contained exactly one '1', otherwise a is 0, b is 'SQUARE' if any of the strings s entered during the loop iterations contained more than one '1', otherwise b remains an empty string, n is the total number of inputs provided by the user over all iterations, j is 0, and s is the last input string provided by the user.
#Overall this is what the function does:The function processes up to 100 test cases. For each test case, it reads an integer n followed by an n x n grid of '0's and '1's. The function determines whether the grid contains exactly one triangle or one square that includes all '1's, with the size of the shape being greater than 1. If a triangle is found, it prints 'TRIANGLE'; if a square is found, it prints 'SQUARE'. If neither shape is found, it prints an appropriate message indicating no valid shape was identified.

