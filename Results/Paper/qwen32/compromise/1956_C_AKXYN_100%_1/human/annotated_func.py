#State of the program right berfore the function call: Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix a filled with zeroes. The number of test cases t is between 1 and 500, and the sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: The final output state consists of the concatenated outputs for each of the `t` test cases, where each test case outputs `res` (calculated as the sum of `(i + 1) * (2 * i + 1)` for `i` from 0 to `n-1`), `n << 1`, and a series of commands for `n` down to 1, each command printing a row of the matrix twice.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the size of an `n × n` matrix. For each test case, it calculates a specific value `res` and prints this value along with `n << 1`. It then prints a series of commands that describe operations on the matrix, effectively simulating filling the matrix in a specific pattern twice for each row from `n` down to `1`.

