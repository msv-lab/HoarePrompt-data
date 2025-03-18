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
        
    #State: The loop will execute for each test case defined by `t`. For each test case, `n` will be processed according to the given conditions. After all iterations, `res` will be the sum of `(i + 1) * (2 * i + 1)` for all `i` from 0 to `n-1` across all test cases. The value of `total` will be the cumulative sum of all `res` values from each test case. The variable `t` will remain within the range \(1 \leq t \leq 500\). The matrix `mat` will be printed as specified, but its final state will not affect the output value of `res`. The variable `n` must be greater than or equal to 10 for the last observed state, and it can vary for different test cases.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (1 ≤ t ≤ 500) and an integer `n` (1 ≤ n ≤ 500). For each test case, it calculates the sum `res` of the expression `(i + 1) * (2 * i + 1)` for all `i` from 0 to `n-1`, prints this sum along with `n << 1`, and then prints a sequence of operations involving the integers from 1 to `n`. The function returns the total sum of all `res` values across all test cases.

