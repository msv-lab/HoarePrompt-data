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
        
    #State: The loop will process each test case and print the output for each one. The variables `cntl` and `c` will be reset for each test case. After all iterations of the loop, the variables `t`, `n`, and `a` will retain their last values from the last test case, and `cntl` will be a list of counts for the last test case, but `c` will be 0 or the minimum value between 2 and the count of 0s in `a` for the last test case. The specific values of `n` and `a` will depend on the last test case input.
#Overall this is what the function does:The function processes a series of test cases. Each test case consists of an integer `n` and a list of `n` integers. For each test case, the function counts the occurrences of each integer in the list. If there are no zeros in the list, it prints `0`. Otherwise, it prints the smallest index `j` (1 ≤ j ≤ n) such that the count of `j` is less than 2, or `n` if no such index exists. The function does not return any values; it only prints the results for each test case. After processing all test cases, the variables `n` and `a` will retain their values from the last test case, and `cntl` will be a list of counts for the last test case.

