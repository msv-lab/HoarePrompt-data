#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an array `c` of length `n` where each element is a positive integer (1 ≤ c_i ≤ 10^9), and a list of `q` queries, each query being a pair of integers `(l_i, r_i)` (1 ≤ l_i ≤ r_i ≤ n). The function should also handle the constraints that the sum of `n` over all test cases does not exceed 3 · 10^5, and the sum of `q` over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop iterates over multiple test cases, and for each test case, it processes an array `c` and a list of queries. After processing all the queries for a test case, the loop moves to the next test case. The variables `n`, `m`, `l`, `p`, `c`, `i`, `j`, `a`, `b`, and `s` are updated within the loop, but their final values at the end of the loop depend on the specific input for each test case. The output state of these variables is not predictable without the actual input data. However, the loop will have printed 'YES' or 'NO' for each query based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an array `l` of positive integers and a list of queries `q`, where each query is a pair of integers `(l_i, r_i)`. The function then computes and prints 'YES' or 'NO' for each query based on the conditions: if the subarray `l[l_i-1:r_i]` contains more than one element and the sum of the subarray minus the length of the subarray is greater than or equal to the count of 1s in the subarray, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any values, and the final state of the program is that all queries for all test cases have been processed and the corresponding results have been printed.

