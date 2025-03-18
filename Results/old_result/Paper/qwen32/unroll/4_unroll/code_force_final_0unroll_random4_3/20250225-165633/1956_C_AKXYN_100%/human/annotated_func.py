#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix filled with zeroes. The number of test cases t (1 ≤ t ≤ 500) is given at the start, and the sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: A sequence of outputs for each test case, where each test case outputs a line with `res` and `2 * n`, followed by `2 * n` lines with the specified format.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`. For each test case, it calculates a value `res` and prints it along with `2 * n`. It then prints `2 * n` lines, each describing operations on a matrix of size `n x n`.

