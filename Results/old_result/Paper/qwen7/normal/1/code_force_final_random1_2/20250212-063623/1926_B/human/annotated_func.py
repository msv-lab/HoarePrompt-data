#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the input consists of n lines, each containing n characters that are either '0' or '1', and the grid contains exactly one triangle or exactly one square that includes all the '1's in the grid, with the size of the triangle or square being greater than 1.
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
        
    #State: Postcondition: `i` is equal to `a`, `k` is a list containing the total count of '1's from all input strings provided across all iterations, and `b` is the last input string received. If the first element of `k` is equal to the second element of `k`, the condition holds as is. If the first element of `k` is not equal to the second element of `k`, the condition also holds as is.
#Overall this is what the function does:The function processes multiple grids, each defined by a series of lines containing '0' and '1'. For each grid, it counts the number of '1's in each line and determines whether these '1's form a square or a triangle. It then prints 'SQUARE' if the shape is a square, and 'TRIANGLE' if the shape is a triangle. The function does not return any value but prints the result for each grid processed.

