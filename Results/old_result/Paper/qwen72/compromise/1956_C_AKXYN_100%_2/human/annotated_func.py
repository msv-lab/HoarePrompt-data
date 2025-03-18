#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, n is an integer such that 1 <= n <= 500.
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
        
    #State: `t` is an integer such that 1 <= t <= 500, `n` is an input integer such that 1 <= n <= 500 and `n` must be greater than 0, `mat` is a list of `n` lists, each containing integers from 1 to `n` inclusive, `res` is the sum of (i + 1) * (2 * i + 1) for i from 0 to n-1, `i` is 0.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by an integer `n` (1 <= n <= 500). For each test case, it creates an `n x n` matrix where each row contains integers from 1 to `n`. It then calculates a result `res` as the sum of `(i + 1) * (2 * i + 1)` for `i` ranging from 0 to `n-1`. The function prints `res` followed by `n` shifted left by 1 bit (i.e., `n * 2`). Additionally, it prints a series of formatted strings for each integer from `n` down to 1, each string containing the integer and a sequence of integers from 1 to `n`. The function does not return any value.

