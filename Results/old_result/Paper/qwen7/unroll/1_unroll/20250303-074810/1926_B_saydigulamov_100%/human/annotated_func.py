#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the grid is represented as a list of n strings, each string contains n characters that are either '0' or '1', and the grid contains exactly one triangle or exactly one square that includes all the '1's in the grid.
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
        
    #State: Output State: The output state depends on the inputs provided during the execution of the loop. For each iteration of the outer loop (controlled by `a`), the code checks if the number of '1's in the first two strings (`b`) are equal. If they are equal, it prints 'SQUARE', otherwise it prints 'TRIANGLE'. The final output state will be a series of lines, each containing either 'SQUARE' or 'TRIANGLE', corresponding to the number of iterations of the outer loop.
#Overall this is what the function does:The function processes a series of grids, each containing exactly one triangle or one square formed by '1's. For each grid, it counts the number of '1's in the first two rows and compares these counts. If the counts are equal, it indicates a square; otherwise, it indicates a triangle. The function outputs 'SQUARE' or 'TRIANGLE' for each grid based on this comparison.

