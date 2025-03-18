#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: For each of the t test cases, the output consists of the lines: 1 1, 1 2, and then for each i from 3 to n, the line i i. The value of t and the values of n for each test case remain unchanged.
#Overall this is what the function does:The function processes `t` test cases, where for each test case it outputs a series of lines. For each test case, it first outputs `1 1` and `1 2`, then for each integer `i` from 3 to `n` (where `n` is the input for that test case), it outputs `i i`. The values of `t` and `n` for each test case remain unchanged.

