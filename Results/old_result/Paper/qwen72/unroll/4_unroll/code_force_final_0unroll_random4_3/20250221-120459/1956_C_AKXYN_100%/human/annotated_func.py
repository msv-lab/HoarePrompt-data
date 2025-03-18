#State of the program right berfore the function call: The function does not take any input parameters, but it is expected to handle multiple test cases. Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the n×n matrix. The number of test cases t is also an integer (1 ≤ t ≤ 500), and the sum of n^2 over all test cases does not exceed 5 · 10^5.
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
        
    #State: The loop has finished executing all iterations for each of the t test cases. For each test case, the variable `res` holds the sum of (i + 1) * (2 * i + 1) for i from 0 to n-1, and the value `n << 1` (which is 2 * n) is printed alongside `res`. Additionally, for each value of i from n down to 1, two lines are printed: the first line starts with '1' followed by i and the range from 1 to n, and the second line starts with '2' followed by i and the range from 1 to n. The variables `t` and `n` retain their values as they were at the start of each test case, but the loop has completed its execution for all test cases.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` (1 ≤ n ≤ 500) representing the size of an n×n matrix. It calculates a value `res` as the sum of (i + 1) * (2 * i + 1) for i from 0 to n-1, and prints `res` followed by `2 * n`. Additionally, for each value of i from n down to 1, it prints two lines: the first line starts with '1' followed by i and the range from 1 to n, and the second line starts with '2' followed by i and the range from 1 to n. The function does not return any values, but it processes and prints results for each test case.

