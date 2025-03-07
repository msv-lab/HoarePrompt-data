#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 500) representing the number of test cases. Each test case consists of a single integer n (1 ≤ n ≤ 500) representing the size of the n x n matrix. It is guaranteed that the sum of n^2 over all test cases does not exceed 5 * 10^5.
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
        
    #State: The loop has executed `t` times, where each iteration processes a matrix of size `n` (as specified by the input). For each test case, `mat` is a list of `n` lists, where each inner list contains integers from 1 to `n`. The variable `res` is calculated as the sum of `(i + 1) * (2 * i + 1)` for `i` from 0 to `n-1`, which simplifies to the formula \(\frac{n(4n^2 + 3n - 1)}{6}\). The variable `i` is 0 at the start of each iteration. The loop prints `res` followed by `n << 1` (which is `2 * n`), and then for each `i` from `n` down to 1, it prints two lines: the first line starting with '1' followed by `i` and the numbers from 1 to `n`, and the second line starting with '2' followed by `i` and the numbers from 1 to `n`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the size of an `n x n` matrix. For each test case, it calculates a specific result based on the formula \(\frac{n(4n^2 + 3n - 1)}{6}\) and prints this result followed by `2 * n`. It then prints a sequence of `2 * n` lines, each representing operations on the matrix, alternating between two types of operations.

