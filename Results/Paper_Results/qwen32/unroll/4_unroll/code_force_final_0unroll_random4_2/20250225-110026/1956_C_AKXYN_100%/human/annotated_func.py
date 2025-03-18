#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n x n matrix filled with zeroes. The function should handle multiple test cases, with the total number of test cases t (1 ≤ t ≤ 500) and the sum of n^2 over all test cases not exceeding 5 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        mat = [list(range(1, n + 1)) for i in range(n)]
        
        res = 0
        
        for i in range(n):
            res += (i + 1) * (2 * i + 1)
        
        print(res, n << 1)
        
        for i in range(n, 0, -1):
            print('1 %d' % i, *range(1, n + 1))
            print('2 %d' % i, *range(1, n + 1))
        
    #State: For each test case with size `n`, the output consists of one line with `res` and `n * 2`, followed by `2 * n` lines with the specified format.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` representing the size of an `n x n` matrix. For each test case, it outputs a specific value `res` and `n * 2`, followed by `2 * n` lines describing operations on the matrix.

