#State of the program right berfore the function call: The function should take a list of strings as input, where each string represents a row in the n x n binary grid, and n is an integer such that 2 ≤ n ≤ 10. The grid contains exactly one triangle or one square, and the shape cannot consist of exactly one 1. The function should return "SQUARE" if the shape is a square, and "TRIANGLE" if the shape is a triangle.
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
        
    #State: The value of `a` remains unchanged, and `k` is an empty list after each iteration of the outer loop. The function will print 'SQUARE' or 'TRIANGLE' for each grid based on the counts of '1's in the rows.
#Overall this is what the function does:The function `func` reads an integer `a` from the user, representing the number of grids to process. For each grid, it reads `n` (an integer) from the user, where `n` is the size of the n x n binary grid. It then reads `n` strings, each representing a row in the grid. The function counts the number of '1's in each row that contains at least one '1'. If the count of '1's in the first row that contains '1's is equal to the count in the second row, it prints 'SQUARE'. Otherwise, it prints 'TRIANGLE'. After processing each grid, the function resets and continues to the next grid. The value of `a` remains unchanged throughout the function execution. The function does not return any value; it only prints the shape for each grid.

