#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the grid is an n × n list of strings, where each string consists of n characters that are either '0' or '1'; the grid contains exactly one triangle or exactly one square that contains all the '1's in the grid; the size of the triangle or square is greater than 1 (i.e., the shape cannot consist of exactly one '1').
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
        
    #State: t is the initial input integer (1 ≤ t ≤ 100), i is t-1, n is the input integer for the last test case, a is 'TRIANGLE' if the last string s of the last test case contains exactly one '1', otherwise a is 0, b is 'SQUARE' if any string s of the last test case contains more than one '1', otherwise b is '', and j is n-1. The final printed output is 'TRIANGLE' if a is not 0, otherwise it is 'SQUARE'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an `n × n` grid of '0's and '1's. It determines whether the '1's form a triangle or a square and outputs the type of shape for each test case.

