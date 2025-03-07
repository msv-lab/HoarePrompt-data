#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 2 <= n <= 10, and the grid is an n x n list of lists where each element is either '0' or '1'. The grid contains exactly one triangle or exactly one square that consists of all the '1's, and the size of the shape (k) is greater than 1.
def func():
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print('SQUARE')
        else:
            print('TRIANGLE')
        
    #State: The output state after all iterations will be a series of 'SQUARE' or 'TRIANGLE' prints, depending on the shape represented by the input lines for each iteration. The state of `t`, `n`, and `grid` remains unchanged.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and an `n x n` grid of '0's and '1's. It determines whether the '1's in the grid form a square or a triangle and prints 'SQUARE' or 'TRIANGLE' accordingly for each test case.

