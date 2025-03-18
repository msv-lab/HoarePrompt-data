#State of the program right berfore the function call: The function should be called with a grid represented as a list of lists, where each inner list contains n characters '0' or '1', and n is an integer such that 2 ≤ n ≤ 10. The grid contains exactly one triangle or exactly one square that includes all the '1's, and the shape's size is greater than 1. The function should also handle multiple test cases, where the number of test cases t is an integer such that 1 ≤ t ≤ 100.
def func():
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print(k)
        
    #State: The loop iterates `a` times, and for each iteration, it reads an integer `n` and then `n` lines of input representing a grid. If any of these grids contain exactly two rows with the same number of '1's, it prints a list of the counts of '1's in those rows. The state of the other variables in the precondition that are not affected by the loop head and body remains unchanged.
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads an integer `n` representing the number of rows in a grid, followed by `n` lines of input, each containing a string of characters '0' or '1'. If any of these grids contain exactly two rows with the same number of '1's, it prints a list of the counts of '1's in those rows. The function does not return any value. The state of the program after the function concludes is unchanged except for the side effect of printing the results to the console.

