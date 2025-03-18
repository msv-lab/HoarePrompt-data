#State of the program right berfore the function call: The function does not take any input parameters, but it is designed to work with multiple test cases where each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of an n×n matrix. The number of test cases t is an integer (1 ≤ t ≤ 500), and the sum of n^2 over all test cases does not exceed 5 \cdot 10^5.
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
        
    #State: The loop has completed all iterations, `n` remains unchanged, `i` is 0, `res` is the sum of `(i + 1) * (2 * i + 1)` for all `i` from 0 to `n-1`, and the matrix `mat` is an n×n matrix filled with integers from 1 to n in each row.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` (1 ≤ n ≤ 500) representing the size of an n×n matrix. For each test case, it calculates and prints a value `res` which is the sum of `(i + 1) * (2 * i + 1)` for all `i` from 0 to `n-1`, followed by the value `n << 1` (which is `2 * n`). It then prints two lines for each row of the matrix, where the first line starts with '1' and the second line starts with '2', followed by the row number and the integers from 1 to `n`. The function does not return any values; it only prints the results to the console. After processing all test cases, the function concludes, and the state of the program is such that all test cases have been processed and their results printed.

