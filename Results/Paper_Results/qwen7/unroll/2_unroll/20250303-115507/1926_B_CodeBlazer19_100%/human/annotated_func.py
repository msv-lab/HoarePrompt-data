#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 2 ≤ n ≤ 10, and the grid is represented as a list of n strings, each string containing n characters that are either '0' or '1'. The grid contains exactly one triangle or exactly one square that includes all the '1's in the grid, and the size of the triangle or square is greater than 1.
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
        
    #State: Output State: `t` integers are inputted. For each integer `n`, `n` strings are inputted. If any string has exactly one '1', the output is 'TRIANGLE'. Otherwise, the output is 'SQUARE'. The final output consists of either 'TRIANGLE' or 'SQUARE' for each input pair (n, strings).
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a grid represented as a list of strings. Each string contains binary characters ('0' or '1'). The function determines whether the grid contains a triangle or a square that includes all the '1's and prints 'TRIANGLE' if a triangle is found, otherwise it prints 'SQUARE'. The function does not return any value but prints the result for each test case.

