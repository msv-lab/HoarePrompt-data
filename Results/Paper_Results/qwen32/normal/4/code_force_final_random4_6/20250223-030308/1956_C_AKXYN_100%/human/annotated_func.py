#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 500) representing the number of test cases. For each test case, there is a single integer n (1 ≤ n ≤ 500) representing the size of the matrix a. The sum of n^2 over all test cases does not exceed 5 \cdot 10^5.
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
        
    #State: The final output state includes the values of `res` and `2 * n` for the last test case, followed by the series of commands involving the matrix rows for the last test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves an integer `n` representing the size of an `n x n` matrix. For each test case, it calculates a specific result `res` based on the formula `(i + 1) * (2 * i + 1)` summed over all `i` from `0` to `n-1`. It then prints this result along with `2 * n`. Following this, it outputs a series of commands involving the matrix rows, printing each row twice with different labels ('1' and '2'). The final output for each test case includes the calculated result and the series of commands for the last test case.

