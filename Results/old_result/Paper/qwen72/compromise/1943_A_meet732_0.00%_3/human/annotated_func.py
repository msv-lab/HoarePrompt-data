#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case consists of an integer n (1 ≤ n ≤ 2 · 10^5) and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i < n). The total number of test cases, t, should satisfy 1 ≤ t ≤ 2 · 10^4, and the sum of n over all test cases should not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: The loop has completed all iterations, and for each test case, the output is the first index `j` (starting from 1) where `cntl[j]` is less than 2, or `n` if no such index exists. If `cntl[0]` is 0, the output is 0 for that test case.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case consists of an integer `n` and a list of `n` integers. For each test case, the function outputs the first index `j` (starting from 1) where the count of `j` in the list is less than 2, or `n` if no such index exists. If the count of 0 in the list is 0, the function outputs 0 for that test case. The function does not return any values; it only prints the results.

