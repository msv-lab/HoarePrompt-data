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
        
    #State: Postcondition: `t` is an integer such that \(1 \leq t \leq 100\), `a` is an integer greater than 0, `i` is the total number of iterations the loop has executed (which is equal to `a`), `k` is a list containing the cumulative count of '1's in the binary representation of all integers provided as input through the loop, and `b` is the most recent input string from the user. If the first element of `k` is equal to the second element of `k`, the program prints 'SQUARE'. If the first element of `k` is not equal to the second element of `k`, the program prints 'TRIANGLE'.
#Overall this is what the function does:The function processes up to 100 test cases, where each test case consists of an integer n (2 ≤ n ≤ 10) and an n x n grid of characters ('0' or '1'). It determines whether the grid contains a triangle or a square that includes all the '1's and prints 'SQUARE' or 'TRIANGLE' accordingly for each test case. After processing all test cases, the function does not return any value but prints the type of shape found for each test case.

