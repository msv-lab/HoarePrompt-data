#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix a filled with zeroes. The input consists of multiple test cases, with the first line containing the number of test cases t (1 ≤ t ≤ 500). The sum of n^2 over all test cases does not exceed 5 · 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum, r = 0, 0
        
        for i in range(1, n + 1):
            if n * (n + 1) // 2 > i * n:
                r = i
                sum += n * (n + 1) // 2
            else:
                sum += i * n
        
        print(sum, n + r)
        
        for j in range(1, n + r + 1):
            if j <= n:
                print(1, j, end=' ')
                print(*range(1, n + 1))
            else:
                print(2, j % n, end=' ')
                print(*range(1, n + 1))
        
    #State: For each test case, the final value of `sum` and `n + r` are printed, followed by a series of lines starting with either `1` or `2`, followed by an index and the sequence `1` to `n`. The size of the matrix `a` and the value of `t` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the size of an n × n matrix. For each test case, it calculates and prints a sum and a value `n + r`, followed by a series of lines that describe operations to fill the matrix. The matrix itself is not returned or modified; only the described operations are printed.

