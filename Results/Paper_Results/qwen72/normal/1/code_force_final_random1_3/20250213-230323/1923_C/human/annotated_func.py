#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and q are integers where 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where 1 ≤ c_i ≤ 10^9; l_i and r_i are integers for each query where 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 · 10^5; the sum of q over all test cases does not exceed 3 · 10^5.
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
        
    #State: After all iterations of the loop, the variable `_` has been decremented to 0, indicating that all test cases have been processed. The lists `p` and `c` have been updated to contain the cumulative sums and counts of 1s, respectively, for each list `l` of integers provided in the input. The variables `n` and `m` retain their values as the number of elements in `l` and the number of queries, respectively, for each test case. The variables `i` and `s` are updated for each query based on the cumulative sums and counts stored in `p` and `c`. For each query, if the conditions `b - a + 1 > 1` and `s - (b - a + 1) >= i` are met, 'YES' is printed; otherwise, 'NO' is printed. The final state of the loop is such that all test cases and their respective queries have been processed, and the appropriate outputs have been generated for each query.
#Overall this is what the function does:The function processes multiple test cases, each involving a list of integers and a set of queries. For each test case, it reads the number of elements `n` and the number of queries `m`. It then reads a list of `n` integers. The function computes two cumulative lists: one for the sum of the elements (`p`) and another for the count of 1s (`c`). For each query, it checks if the segment of the list meets a specific condition and prints 'YES' or 'NO' accordingly. After processing all test cases and their queries, the function has no return value but has printed the results for each query.

