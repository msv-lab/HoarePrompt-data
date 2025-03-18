#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the grid is represented as a list of n strings, each string contains n characters which are either '0' or '1', and the grid contains exactly one triangle or exactly one square that includes all the '1's in the grid.
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
        
    #State: Output State: The output state depends on the values of `t` and `a`. For each iteration of the outer loop (controlled by `a`), the program reads multiple strings from input. If the first two strings contain the same number of '1's, it prints 'SQUARE'; otherwise, it prints 'TRIANGLE'. This process repeats `a` times, and the final output is the sequence of 'SQUARE' or 'TRIANGLE' printed during these iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a grid represented as a list of n strings containing '0's and '1's. For each test case, it checks if the grid contains exactly one triangle or exactly one square that includes all the '1's. If the first two strings in the grid contain the same number of '1's, it prints 'SQUARE'; otherwise, it prints 'TRIANGLE'. This process repeats for each test case specified by the user, and the final output is a sequence of 'SQUARE' or 'TRIANGLE' based on the grid analysis for each test case.

