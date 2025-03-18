#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where each element c_i satisfies 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 · 10^5; the sum of q over all test cases does not exceed 3 · 10^5.
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
        
    #State: After all iterations, `t` remains an integer such that 1 ≤ t ≤ 10^4, representing the total number of test cases. Each test case has been fully processed, meaning for each test case, `n` and `m` were read, `l` was a list of integers, `p` and `c` were lists constructed based on cumulative sums and counts of `1`s in `l`, and `m` queries were processed. The final values of `i` and `j` reflect the sum of all elements in `l` and the count of `1`s in `l` from the last processed test case. The variables `a` and `b` hold the values from the last query processed in the last test case, and `s` holds the sum of elements in `l` from index `a` to `b` for that last query. All queries for all test cases have been evaluated, and 'YES' or 'NO' has been printed accordingly.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines whether a specific condition is met regarding the sum and count of ones in a sub-list defined by the query range, and prints 'YES' or 'NO' accordingly.

