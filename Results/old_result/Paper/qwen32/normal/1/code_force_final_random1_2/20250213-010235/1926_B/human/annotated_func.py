#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 2 ≤ n ≤ 10, and the grid is an n × n list of strings where each string consists of n characters, each character being either '0' or '1'. The grid contains exactly one triangle or exactly one square composed of '1's, and the size of the shape (k) is greater than 1.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 100, `n` is an integer such that 2 ≤ n ≤ 10, `grid` is an n × n list of strings where each string consists of n characters, each character being either '0' or '1', and the grid contains exactly one triangle or exactly one square composed of '1's, and the size of the shape (k) is greater than 1, `a` is an input integer, `i` is equal to `a`, and the program has printed "SQUARE" or "TRIANGLE" `a` times based on the input strings.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and an `n × n` grid of strings composed of '0's and '1's. It then determines whether the grid contains exactly one triangle or exactly one square composed of '1's and prints "SQUARE" or "TRIANGLE" accordingly.

