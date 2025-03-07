#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 2 ≤ n ≤ 10, and the grid is an n × n list of strings, where each string consists of n characters that are either '0' or '1'. The grid contains exactly one triangle or exactly one square composed of '1's, and the size of the shape (k) is greater than 1.
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
        
    #State: - The loop will continue to execute until it has completed `a` iterations.
    #   - Each iteration independently processes its own set of input lines and prints "SQUARE" or "TRIANGLE" based on the comparison of the first two counts in `k` for that iteration.
    #   - The state of `t`, `n`, `grid`, and `a` remains unchanged throughout the loop execution except for the variable `i` in the loop header which simply tracks the current iteration number.
    #
    #### Conclusion:
    #- The final output state will consist of `a` print statements, each being either "SQUARE" or "TRIANGLE", depending on the comparison of the first two counts of '1's in the lines read during each iteration.
    #
    #### Final Output State:
    #Output State:
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and an `n × n` grid of strings composed of '0's and '1's. It determines whether the grid contains a square or a triangle made up of '1's and prints "SQUARE" or "TRIANGLE" accordingly for each test case.

