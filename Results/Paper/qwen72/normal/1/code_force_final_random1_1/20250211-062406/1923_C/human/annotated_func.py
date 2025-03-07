#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and q are integers where 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are integers where 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5, and the sum of q over all test cases does not exceed 3 · 10^5.
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
        
    #State: After all iterations of the loop, `t` is decremented by the number of test cases executed, `m` is 0 for the current test case, `a` and `b` are the last values provided by the user input for the current test case, `i` is equal to `c[b] - c[a - 1]` with the final values of `a` and `b`, and `s` is equal to `p[b] - p[a - 1]` with the final values of `a` and `b`. The conditions for printing 'YES' or 'NO' are evaluated based on these final values of `a` and `b`. All other variables (`n`, `l`, `p`, `c`, `j`) remain unchanged for the current test case, but will be reinitialized for the next test case if any.
#Overall this is what the function does:The function processes multiple test cases, each involving a list of integers and a set of queries. For each query, it determines whether a specific condition is met within a specified range of the list and prints 'YES' or 'NO' accordingly. The function reads input from the user for the number of test cases, the size of the list, the list itself, and the queries. It maintains internal state for each test case but resets it for the next test case. The final state after the function concludes is that all test cases have been processed, and the appropriate 'YES' or 'NO' responses have been printed for each query.

