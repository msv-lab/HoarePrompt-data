#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and q are integers where 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where 1 ≤ c_i ≤ 10^9; queries is a list of q pairs (l_i, r_i) where 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5, and the sum of q over all test cases does not exceed 3 · 10^5.
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
        
    #State: After all iterations of the loop, `t` is decremented by the number of test cases processed, `n` and `q` remain as initially defined, `l` is the list of integers from user input, `p` is a list where each element is the cumulative sum of elements in `l` up to that point, starting with `[0]`, `c` is a list where each element is the cumulative count of `1`s in `l` up to that point, starting with `[0]`, `i` and `j` are the final counts of the cumulative sums and `1`s respectively, `a` and `b` are the last pair of integers from user input, `s` is the difference `p[b] - p[a - 1]`, and `m` is 0. For each query, if `b - a + 1 > 1` and `s - (b - a + 1) >= i`, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function processes multiple test cases, each involving a list of integers and a set of queries. For each test case, it reads the length of the list and the number of queries, then the list itself. It computes two cumulative lists: one for the sum of elements (`p`) and another for the count of ones (`c`). For each query, it checks a condition based on these cumulative lists and prints 'YES' or 'NO' accordingly. The function does not return any value; it only prints the results of the queries.

