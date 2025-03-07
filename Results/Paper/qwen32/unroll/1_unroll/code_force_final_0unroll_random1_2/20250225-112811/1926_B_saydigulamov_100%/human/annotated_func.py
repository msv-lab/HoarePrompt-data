#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 2 <= n <= 10, and the grid is an n x n list of lists containing only the characters '0' or '1'. Each grid contains exactly one triangle or exactly one square that consists of all the '1's in the grid, and the size of the shape (k) is greater than 1.
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
        
    #State: the loop will print 'SQUARE' or 'TRIANGLE' for each of the `a` iterations, and `t`, `n`, and the grid will remain unchanged.
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads an integer `n` and an `n x n` grid of characters '0' or '1'. It then determines and prints whether the shape formed by the '1's in the grid is a 'SQUARE' or a 'TRIANGLE'. The input values `a`, `n`, and the grid remain unchanged after the function execution.

