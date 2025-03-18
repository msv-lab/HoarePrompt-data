#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix a filled with zeroes. The number of test cases t satisfies 1 ≤ t ≤ 500, and the sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: The output will be a series of printed lines for each test case, with the final printed lines being the result of the last test case. Specifically, it will be `res` and `2 * n` followed by the patterns printed in the nested loops for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` representing the size of an `n × n` matrix. For each test case, it calculates and prints a specific result based on `n`, followed by a series of formatted lines indicating patterns related to the matrix size.

