#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the grid is represented as a list of n strings, each string contains n characters which are either '0' or '1', and the grid contains exactly one triangle or exactly one square that contains all the '1's in the grid.
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
        
    #State: After all iterations, `k` is a list containing the total count of '1's across all input strings provided during the loop executions. If the first element of `k` is equal to the second element of `k`, the condition inside the if block is true, and 'SQUARE' is printed for each iteration. Otherwise, the condition inside the else block is executed, and 'TRIANGLE' is printed for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a grid represented as a list of strings containing '0's and '1's. For each grid, it counts the number of '1's in each row and checks if the counts match. If the counts match, it prints 'SQUARE'; otherwise, it prints 'TRIANGLE'. The function does not return any value but prints 'SQUARE' or 'TRIANGLE' based on the grid configuration. If no valid shape is found or multiple shapes are present, it will print an error message.

