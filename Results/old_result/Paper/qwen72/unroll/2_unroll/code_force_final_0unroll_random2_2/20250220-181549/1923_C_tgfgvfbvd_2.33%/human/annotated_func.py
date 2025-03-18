#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an array `c` of length `n` where each element is a positive integer (1 ≤ c_i ≤ 10^9), and `q` queries where each query is defined by two integers `l_i` and `r_i` (1 ≤ l_i ≤ r_i ≤ n). The total number of test cases `t` is a positive integer (1 ≤ t ≤ 10^4), and the sum of `n` and `q` over all test cases does not exceed 3 · 10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = []
        
        c = 0
        
        for x in l:
            c += x
            p.append(c)
        
        for _ in range(m):
            a, b = map(int, input().split())
            s = p[b - 1]
            if a - 2 >= 0:
                s -= p[a - 2]
            if b - a + 1 > 1 and s >= 2 * (b - a + 1):
                print('YES')
            else:
                print('NO')
        
    #State: The loop has finished executing all iterations. The variables `n`, `m`, `l`, `p`, `a`, `b`, and `c` have been updated and used during the execution of the loop, but their final values are not retained for the next test case. The loop processes each test case independently, and the output for each query is either 'YES' or 'NO' based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an array `l` of positive integers and a set of queries. For each query defined by two integers `a` and `b`, the function checks if the sum of elements in the prefix sum array `p` from index `a-1` to `b-1` is at least twice the length of the subarray. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any values but outputs the results directly. The state of the program after the function concludes is that all test cases have been processed, and the output for each query has been printed. The variables used within each test case are reset for the next test case, ensuring independent processing.

