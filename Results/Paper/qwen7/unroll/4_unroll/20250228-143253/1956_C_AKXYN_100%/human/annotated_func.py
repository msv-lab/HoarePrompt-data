#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: Output State: t test cases are printed, each followed by two lines of output. For each test case:
    #1. A line containing the value of `res` and `n << 1`.
    #2. `n` lines, each starting with '1' followed by numbers from 1 to n.
    #3. `n` lines, each starting with '2' followed by numbers from 1 to n.
    #
    #The value of `res` is calculated as the sum of `(i + 1) * (2 * i + 1)` for each row `i` in the matrix `mat`, and `n << 1` is equivalent to `2 * n`. The matrix `mat` is a square matrix of size `n x n` filled with numbers from 1 to n in sequence.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer \( n \) (where \( 1 \leq n \leq 500 \)). For each test case, it calculates a value \( res \) as the sum of \((i + 1) \times (2 \times i + 1)\) for each row \( i \) in a square matrix of size \( n \times n \), and prints \( res \) along with \( 2n \). It then prints \( n \) lines starting with '1' followed by numbers from 1 to \( n \), and another \( n \) lines starting with '2' followed by numbers from 1 to \( n \).

