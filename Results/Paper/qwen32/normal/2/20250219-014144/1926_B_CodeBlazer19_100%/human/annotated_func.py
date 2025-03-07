#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the grid is an n × n list of lists where each element is either '0' or '1'; the grid contains exactly one triangle or exactly one square made up of '1's, and the size of the shape (k) is greater than 1.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = 0
        
        b = ''
        
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'TRIANGLE'
            elif s.count('1') > 1:
                b = 'SQUARE'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: The variable `i` will be equal to `t`, `a` will be `'TRIANGLE'` if any row in any test case had exactly one '1', otherwise `a` will be 0, `b` will be `'SQUARE'` if any row in any test case had more than one '1', otherwise `b` will be an empty string, `n` will be the last input integer read before the loop ends, and `j` will be equal to `n`. Each test case will print either `'TRIANGLE'` or `'SQUARE'` based on the conditions specified.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an n × n grid of '0's and '1's. It determines whether the grid contains a shape formed by '1's that resembles a triangle or a square and prints 'TRIANGLE' or 'SQUARE' accordingly for each test case.

