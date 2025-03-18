#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an array `c` of length `n` where each element is a positive integer (1 ≤ c_i ≤ 10^9), and `q` queries. For each query, two integers `l_i` and `r_i` are provided (1 ≤ l_i ≤ r_i ≤ n) representing the start and end indices of a subarray of `c`. The function should determine if each subarray is "good" based on the conditions specified in the problem description. The number of test cases `t` is a positive integer (1 ≤ t ≤ 10^4), and the sum of `n` and `q` over all test cases does not exceed 3 · 10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [0]
        
        c = [0]
        
        i, j = 0, 0
        
        for x in l:
            if x == 1:
                j += 1
            i += x
            p.append(i)
            c.append(j)
        
        for _ in range(m):
            a, b = map(int, input().split())
            i = c[b] - c[a - 1]
            s = p[b] - p[a - 1]
            if b - a + 1 > 1 and s - (b - a + 1) >= i:
                print('YES')
            else:
                print('NO')
        
    #State: The function `func` will have processed all test cases. For each test case, it will have computed and printed 'YES' or 'NO' for each query based on the conditions specified in the loop. The variables `n`, `m`, `l`, `p`, `c`, `i`, `j`, `a`, and `b` will have been updated and used during the execution of the loop, but their final values will not be relevant to the output state.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an array of positive integers and a series of queries. For each query, it determines and prints whether the specified subarray is "good" based on the condition that the sum of the subarray minus the length of the subarray is greater than or equal to the count of ones in the subarray, provided the subarray length is greater than 1. If the condition is not met, it prints 'NO'. The function does not return any values, and the final state of the program after the function concludes is that all test cases have been processed and the results for each query have been printed.

