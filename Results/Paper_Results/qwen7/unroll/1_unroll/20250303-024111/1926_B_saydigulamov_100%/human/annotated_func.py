#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the input consists of t test cases, each test case starts with an integer n followed by n lines, each containing n characters that are either '0' or '1', and the grid contains exactly one triangle or exactly one square that includes all the '1's in the grid, with the size of the triangle or square being greater than 1.
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
        
    #State: The output will be either 'SQUARE' or 'TRIANGLE' printed for each test case based on the condition given in the loop. Each test case's result is determined by the count of '1's in the input strings. If the counts of '1's in the first two strings are equal, it prints 'SQUARE', otherwise 'TRIANGLE'. The exact sequence of 'SQUARE' and 'TRIANGLE' depends on the input provided during the execution of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid of '0's and '1's. For each test case, it checks if the grid contains exactly one triangle or one square that includes all the '1's, with the size of the shape being greater than 1. Based on the configuration of '1's, it prints either 'SQUARE' or 'TRIANGLE' for each test case. The function does not return any value but prints the results for each test case.

