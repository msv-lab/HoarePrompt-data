#State of the program right berfore the function call: The function does not take any input parameters. However, it is expected to handle multiple test cases, each with an integer n (1 ≤ n ≤ 500) representing the size of the matrix a, and the number of test cases t (1 ≤ t ≤ 500) is provided in the input. The sum of n^2 over all test cases does not exceed 5 \cdot 10^5.
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
        
    #State: The loop has finished executing all iterations. The variable `res` for each test case will hold the value of the sum of (i + 1) * (2 * i + 1) for i from 0 to n-1, and the value of `n << 1` will be printed alongside `res`. Additionally, for each test case, two lines are printed for each value of i from n to 1: the first line starts with '1' followed by the value of i and the range from 1 to n, and the second line starts with '2' followed by the value of i and the range from 1 to n. The matrix `mat` and the loop variable `_` are not relevant to the final output state.
#Overall this is what the function does:The function `func` processes multiple test cases, each specified by an integer `n` (1 ≤ n ≤ 500). For each test case, it calculates a value `res` which is the sum of (i + 1) * (2 * i + 1) for i from 0 to n-1, and prints `res` alongside the value of `n << 1`. Additionally, for each value of `i` from `n` to 1, it prints two lines: the first line starts with '1' followed by `i` and the range from 1 to `n`, and the second line starts with '2' followed by `i` and the range from 1 to `n`. The function does not return any values; it only prints the results.

