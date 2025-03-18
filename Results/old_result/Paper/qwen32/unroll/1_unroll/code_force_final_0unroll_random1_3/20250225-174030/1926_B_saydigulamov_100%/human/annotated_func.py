#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 2 ≤ n ≤ 10, and the grid is an n × n list of lists where each element is either '0' or '1'. The grid contains exactly one triangle or exactly one square that consists of all '1's, and the size of this shape is greater than 1.
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
        
    #State: The output state consists of `a` lines, each being either "SQUARE" or "TRIANGLE", depending on the counts of '1's in the input strings for each iteration. The values of `t`, `n`, and `grid` remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and an `n × n` grid of '0's and '1's. It then determines whether the grid contains exactly one square or one triangle made up entirely of '1's and outputs "SQUARE" or "TRIANGLE" accordingly. The values of `t`, `n`, and the grid remain unchanged.

