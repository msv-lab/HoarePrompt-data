#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 2 ≤ n ≤ 10, and the grid is an n × n list of strings where each string consists of n characters, each character being either '0' or '1'. The grid contains exactly one triangle or exactly one square that contains all the '1's in the grid, and the size of the triangle or square is greater than 1.
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
        
    #State: `i` is equal to `a`; `k` is a list containing the counts of '1's from each of the input strings `b` that contain '1's in the last iteration; `b` is the last input string processed by the loop. If the count of '1's in the first input string `b[0]` is equal to the count of '1's in the second input string `b[1]` in the last iteration, then `k[0]` is equal to `k[1]`. Otherwise, the count of '1's in `b[0]` is not equal to the count of '1's in `b[1]`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and an `n × n` grid of strings composed of '0's and '1's. It determines whether the '1's in the grid form a square or a triangle and prints 'SQUARE' or 'TRIANGLE' accordingly for each test case.

